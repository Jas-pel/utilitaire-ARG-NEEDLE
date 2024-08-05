# Importer les bibliothèques nécessaires
suppressPackageStartupMessages({
    library(argparse)
    options(encoding = "latin1")
    library(bigsnpr)
    library(data.table)
})

# Définir les arguments en ligne de commande
parser <- ArgumentParser(description = "Interpolate genetic position using a GRCh38 reference Hapmap reference")
parser$add_argument("-map", type = "character", help = ".map file to generate genetic positions in")
parser$add_argument("-ref_dir", type = "character", default = "/lustre03/project/6033529/IBD_epilepsy/data/genetic_map_grch38", help = "Directory where the Hapmap PLINK files are found [default \"%(default)s\"]")
parser$add_argument("-cores", type = "integer", default = 1, help = "Number of cores to be used for computation [default \"%(default)s\"]")
parser$add_argument("-method", type = "character", default = "linear", help = "Method to be used for interpolation (spline or linear) [default \"%(default)s\"]")

# Parser les arguments
args <- parser$parse_args()

if (!args$method %in% c("spline", "linear")) {
    stop("Specified method is not implemented")
}

# Définir la fonction d'interpolation génétique
gen_pos_interpolation_grch38 <- function (infos.pos, dir, method, ncores = 1)
{
    # Utilisation du chromosome 19
    chr <- 19

    # Lecture du fichier de référence .map
    basename <- paste0("plink.chr", chr, ".GRCh38.map") 
    mapfile <- file.path(dir, basename)
    ref_data <- fread(mapfile, header = FALSE)
    
    # Interpolation des positions génétiques
    gen_pos <- snp_split(rep(chr, length(infos.pos)), function(ind.chr, pos, dir, method) {
        pos.chr <- pos[ind.chr]
        ind <- match(pos.chr, ref_data$V4)  # Matching the physical pos found in the reference
        new_pos <- ref_data$V3[ind]  # Genetic pos is extracted for physical pos that are found in the reference
        indNA <- which(is.na(ind))  # Which variants need to be interpolated?
        if (length(indNA) > 0) {
            if (method == "spline") {
                new_pos[indNA] <- suppressWarnings(stats::spline(ref_data$V4,
                    ref_data$V3, xout = pos.chr[indNA], method = "hyman")$y)
            } else {
                new_pos[indNA] <- suppressWarnings(stats::approx(ref_data$V4,
                    ref_data$V3, xout = pos.chr[indNA], yleft = 0, yright = max(ref_data$V3))$y)
            }
        }
        new_pos
    }, combine = "c", pos = infos.pos, dir = dir, method = method, ncores = ncores)
    
    return(gen_pos)
}

# Lecture du fichier .map
map_data <- fread(args$map, header = FALSE)

# Interpolation des positions génétiques
gen_pos <- gen_pos_interpolation_grch38(infos.pos = map_data$V4, dir = args$ref_dir, method = args$method, ncores = args$cores)

# Mise à jour des positions génétiques dans le fichier .map
map_data$V3 <- gen_pos

# Écriture du fichier .map mis à jour
output_file <- paste0(args$map)
fwrite(map_data, output_file, col.names = FALSE, row.names = FALSE, sep = "\t")
