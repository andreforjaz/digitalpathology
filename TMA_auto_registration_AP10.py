# Running decision

M={
'paths':'1',
'load_images':'1',
'auto_reg_setup':'0',
'two_auto_reg':'0',
'centroid_locations':'0',
'crop_blobs':'0',
'individual_blob_registration':'1',#1
'registration_evaluation':'0',#1
'nuclei_detection':'1',
'analysing_data':'1',
'clean_data':'0',
'statistics':'0',
'auto_annot_reslt':'0',
'change_magnification':'0',
'format_CNN':'0'
}


## Paths
if M['paths']== '1' :
    pth = '\\babyserverdw4\Pei-Hsun Wu\digital pathology image data\IF HE co-stain AM\TMA analysis\TMA2';
    pthdata = '\\babyserverdw4\Pei-Hsun Wu\digital pathology image data\IF HE co-stain AM\TMA analysis\TMA2\data TMA2';

    # Load path of image folders
    pthhe = '\\babyserverdw4\Pei-Hsun Wu\digital pathology image data\IF HE co-stain AM\TMA section 2 IF run1 AM\H&E image';
    pthif = '\\babyserverdw4\Pei-Hsun Wu\data from SFC imager\02142020 PW IHC Breast Tumor TMA Imaging take 2 dapi CD8 foxp3 Cd31 panck\well image stitch';

    # Path Saved images
    # 20x IF

    pthdapi = '\\babyserverdw4\Pei-Hsun Wu\data from SFC imager\02142020 PW IHC Breast Tumor TMA Imaging take 2 dapi CD8 foxp3 Cd31 panck\well image stitch\1x_\htcpID309_well01_TMA20200213PW_stitch1_c1_1x_.tif';
    pthcd8 = '\\babyserverdw4\Pei-Hsun Wu\data from SFC imager\02142020 PW IHC Breast Tumor TMA Imaging take 2 dapi CD8 foxp3 Cd31 panck\well image stitch\1x_\htcpID309_well01_TMA20200213PW_stitch1_c2_1x_.tif';
    pthfoxp3 = '\\babyserverdw4\Pei-Hsun Wu\data from SFC imager\02142020 PW IHC Breast Tumor TMA Imaging take 2 dapi CD8 foxp3 Cd31 panck\well image stitch\1x_\htcpID309_well01_TMA20200213PW_stitch1_c3_1x_.tif';
    pthpanck = '\\babyserverdw4\Pei-Hsun Wu\data from SFC imager\02142020 PW IHC Breast Tumor TMA Imaging take 2 dapi CD8 foxp3 Cd31 panck\well image stitch\1x_\htcpID309_well01_TMA20200213PW_stitch1_c4_1x_.tif';

    pth20x = '\\babyserverdw4\Pei-Hsun Wu\digital pathology image data\IF HE co-stain AM\TMA analysis\TMA2\data TMA2';

    print(pth20x)