library(tidyverse)
library(foreign)
library(data.table)
library(tidytable)
library(rlang)
library(here)
library(xlsx)
library(RCurl)


# Start with the simple case- one year 

base_chem_url <- "http://publicfiles.dep.state.fl.us/DWRM/Drinking%20Water%20Data/CHEM/2018/"
chem_types <- c("dbp",
                "inor",
                "rad",
                "sec",
                "soc",
                "voc"
)
filetypes = c(".xlsx", ".zip", ".xls")

missing_data = c()

try_filetypes <- function(base_chem_url, chem_type) {
    #Try to download different filetype
    for(j in filetypes){
      chem_url <- paste(base_chem_url, chem_type, j, sep="")
      if(url.exists(chem_url)){
          print(chem_url)
          return(c(TRUE, chem_url, j))
      }
    }

    print(paste("NO FILE FOUND!", "URL:", chem_url))
    return(c(FALSE))
    
}
check_filetype <- function(url, check_type){
  filetype_index = tail(unlist(gregexpr(pattern='\\.', url)), 1)
  filetype <-  substr(url, filetype_index - 1, nchar(url))
  if(identical(filetype, check_type)){
    return(TRUE)
  }
  return(FALSE)
}
get_chem_file <- function(base_chem_url, filename) {
  url_bool_list <- try_filetypes(base_chem_url, filename)
  file_found <- as.logical(url_bool_list[1])
  filetype_found <- url_bool_list[3]
  filename <- paste(filename, filetype_found, sep="")
  local_filename <- here::here("data", "chem_data", filename)

  if(!(file.exists(local_filename))){
    print("file not downloaded yet...")
    if(isTRUE(file_found)){
      print("File exists on the URL"xfd1)
      chem_url <- url_bool_list[2]
      print("Downloading file....")
      download.file(chem_url, destfile = local_filename)
      is_zip <- check_filetype(chem_url, 'zip')
      if(is_zip){
          print("Zip detected, unzipping...")
          unzip(local_filename, exdir = here::here("data", "chem_data"))
      }
      return(TRUE) 
    }
  }
  return(FALSE)
}
# Move to using loop over all years

  # Values for 2004 through 2018 can be acquired using a loop over base_chem_url values 

year_range <- c("04", "05","06","07","08","09","10","11","12","13","14","15","16","17","18")
historical_chem_files <- c()
chem_files <- c()

for (i in 1:length(year_range)) {
  base_chem_url <-paste("http://publicfiles.dep.state.fl.us/DWRM/Drinking%20Water%20Data/CHEM/20", year_range[i],"/", sep="") 
  #Storing all of your xlsx file names here in form {chem_type}{year}{filetype}}
  for (j in 1:length(chem_types)){

      chem_files[j] <- paste(chem_types[j], year_range[i], sep="")
      found <- get_chem_file(base_chem_url, chem_files[j])
      if(!found){
        missing_data <- append(missing_data, chem_files[j])
      }
  }
  # walk(chem_files, get_chem_file)
  historical_chem_files <- append(historical_chem_files, list(chem_files), after = length(historical_chem_files))
}
print(missing_data)









