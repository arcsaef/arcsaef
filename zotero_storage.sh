#!/usr/bin/bash

IFS=$'\n' # make newline the only separator
base_path="/drives/c/Users/Okpokam/Zotero/storage"
for fldr in `ls $base_path` 
do
  fn=`ls $base_path/"$fldr"`
  echo "/drives/c/Workspace/ztore/$fn"
  cp "$base_path/"$fldr"/$fn" "/drives/c/Workspace/ztore/$fn"
done

