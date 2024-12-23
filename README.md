# AlbumNameOrganiser
Organise the pictures and videos in a directory to have same naming convention via date.

## What it will do:
View the name / creation date / modification date of each of the files and select the lowest from them.

Additionally if an image is located within a subfolder mentioning the year / date and the dates on the image are later than the mentioned date on the folder, then the naming should instead change to have as much from the folder date in the name as possible.
- e.g., if only year 2000 is provided and image is DSC00123, the new name should be 2000_DSC00123.

Furthermore some images instead have describing names. Those shouldn't be changed (e.g., Firefigher / Sügis / etc.).

### File types handled:
- .jpg
- .png
- .mp4
- .MOV
- some raw formats / other image & video formats

### Some potential file namings that need to be converted 
- 20200505_144953 (yyyyMMdd_HHmmss)
- IMG_20200505_144953 (yyyyMMdd_HHmmss)
- PANO_20200505_144953 (yyyyMMdd_HHmmss)
- VID_20200505_144953 (yyyyMMdd_HHmmss)
- video_20200505_144953 (yyyyMMdd_HHmmss)
- received_241244736947430 (not sure if any date is hidden there), but should be somewhere between 2019-2024
- received_-758384546 (not sure if any date is hidden there), but should be somewhere between 2019-2024
- Snapchat-339090659 (not sure if any date is hidden there), but should be somewhere between 2019-2024
- Screenshot_20200505-144953 (yyyyMMdd_HHmmss)
- 1732449301984 (milliseconds in instant)
- signal-2020-05-05-14-49-53-316 (yyyy-MM-dd-HH-mm-ss-SSS)
- non-date-related-naming (e.g., DSC_0002)

### Outcome
- Will need to handle hundreds of GBs of data
- Rename all relevant files to the format: 2020_05_05_144953 (yyyy_MM_dd_HHmmss_SSS)
- File names with meaning are kept as is
