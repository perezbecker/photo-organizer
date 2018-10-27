#!/bin/bash

exiftool "-alldates<filename" ./CreateDateDated_mp4/

rm ./CreateDateDated_mp4/*_original
