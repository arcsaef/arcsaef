#!/usr/bin/bash

IFS=$'\n' # make newline the only separator
for fn in `ls pdf2img`
do
  ocr=$(basename "$fn" | cut -d. -f1)
  echo $ocr
  tesseract pdf2img/"$fn" ocr/"$ocr"
  sleep 3
done
