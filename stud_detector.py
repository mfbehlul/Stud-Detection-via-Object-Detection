import cv2
from PIL import Image
from picamera import PiCamera
from time import sleep
from taliabeeio import TaliaBeeIO
import numpy as np 
io=TaliaBeeIO()
camera=PiCamera()
camera.resolution=(960,720)
sleep(2)
while (True):
    
    io.do9=True #Livebit
    if io.di3==0: 
        camera.capture("/home/pi/Desktop/object_detection_based_colour/foto"+str(sayac)+".png")
        sleep(2)
        
        ## Read and merge
        img = cv2.imread("foto0.png")
        crop_img1=img[540:590,540:590]

        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_1 = cv2.resize(crop_img1, dim, interpolation= cv2.INTER_AREA)
        img_hsv = cv2.cvtColor(resized_1, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_1 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_1 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_1 = cv2.bitwise_or(mask1_1, mask1_1)
        croped_1 = cv2.bitwise_and(resized_1, resized_1, mask=mask_1)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_1=True
        else:
            stud_1=False
        
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("mask_1", mask_1)
        #cv2.imshow("croped_1", croped_1)
        #cv2.imshow("cropped_img1",crop_img1)
        #cv2.imshow("Resized image1", resized_1)





        #-----------------------------------------------------------------------





        crop_img2=img[520:570,710:760]
        

        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_2 = cv2.resize(crop_img2, dim, interpolation= cv2.INTER_AREA)

        #print("Resized2 Dimensions: ", resized_2.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_2, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_2 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_2 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_2 = cv2.bitwise_or(mask1_2, mask2_2)
        croped_2 = cv2.bitwise_and(resized_2, resized_2, mask=mask_2)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>5:
            stud_2=True
        else:
            stud_2=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img2",crop_img2)
        #cv2.imshow("mask_2 ", mask_2)
        #cv2.imshow("croped", croped_2)




        #-----------------------------------------------------------------------





        crop_img3=img[320:370,740:790]


        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_3 = cv2.resize(crop_img3, dim, interpolation= cv2.INTER_AREA)

        #print("Resized3 Dimensions: ", resized_3.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_3, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_3 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_3 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_3 = cv2.bitwise_or(mask1_3, mask1_3)
        croped_3 = cv2.bitwise_and(resized_3, resized_3, mask=mask_3)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_3,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_3=True
            
        else:
            stud_3=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img3",crop_img3)
        #cv2.imshow("mask_3 ", mask_3)
        #cv2.imshow("croped", croped_3)


        #-----------------------------------------------------------------------





        crop_img4=img[135:175,700:750]


        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_4 = cv2.resize(crop_img4, dim, interpolation= cv2.INTER_AREA)

        #print("Resized4 Dimensions: ", resized_4.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_4, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_4 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_4 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_4 = cv2.bitwise_or(mask1_4, mask1_4)
        croped_4 = cv2.bitwise_and(resized_4, resized_4, mask=mask_4)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_4,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_4=True
            
        else:
            stud_4=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img4",crop_img4)
        #cv2.imshow("mask_4 ", mask_4)
        #cv2.imshow("croped", croped_4)



        #-----------------------------------------------------------------------





        crop_img5=img[70:120,690:740]


        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_5 = cv2.resize(crop_img5, dim, interpolation= cv2.INTER_AREA)

        #print("Resized5 Dimensions: ", resized_5.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_5, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_5 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_5 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_5 = cv2.bitwise_or(mask1_5, mask1_5)
        croped_5 = cv2.bitwise_and(resized_5, resized_5, mask=mask_5)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_5,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_5=True
            
        else:
            stud_5=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img5",crop_img5)
        #cv2.imshow("mask_5 ", mask_5)
        #cv2.imshow("croped", croped_5)




        #-----------------------------------------------------------------------





        crop_img6=img[70:110,280:330]


        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_6 = cv2.resize(crop_img6, dim, interpolation= cv2.INTER_AREA)

        #print("Resized6 Dimensions: ", resized_6.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_6, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_6 = cv2.inRange (img_hsv, (0, 14, 19), (30, 89, 127))
        mask2_6 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_6 = cv2.bitwise_or(mask1_6, mask1_6)
        croped_6 = cv2.bitwise_and(resized_6, resized_6, mask=mask_6)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_6,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_6=True
            
        else:
            stud_6=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img6",crop_img6)
        #cv2.imshow("mask_6 ", mask_6)
        #cv2.imshow("croped", croped_6)


        #-----------------------------------------------------------------------





        crop_img7=img[120:160,190:240]


        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_7 = cv2.resize(crop_img7, dim, interpolation= cv2.INTER_AREA)

        #print("Resized7 Dimensions: ", resized_7.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_7, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_7 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_7 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_7 = cv2.bitwise_or(mask1_7, mask1_7)
        croped_7 = cv2.bitwise_and(resized_7, resized_7, mask=mask_7)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_7,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_7=True
        
        else:
            stud_7=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img7",crop_img7)
        #cv2.imshow("mask_7 ", mask_7)
        #cv2.imshow("croped", croped_7)



        #-----------------------------------------------------------------------





        crop_img8=img[360:410,340:390]


        scale_percent = 100 #percent of original size

        width = int(img.shape[1]*scale_percent / 200)
        height = int(img.shape[0]*scale_percent / 200)
        dim = (width, height)

        resized_8 = cv2.resize(crop_img8, dim, interpolation= cv2.INTER_AREA)

        #print("Resized8 Dimensions: ", resized_8.shape)

        #cv2.imshow("Resized image", resized)


        img_hsv = cv2.cvtColor(resized_8, cv2.COLOR_BGR2HSV)

        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        mask1_8 = cv2.inRange (img_hsv, (0, 35, 80), (30, 89, 127))
        mask2_8 = cv2.inRange (img_hsv, (160, 60, 20), (210, 255, 255))

        ## Merge the mask and crop the red regions
        mask_8 = cv2.bitwise_or(mask1_8, mask1_8)
        croped_8 = cv2.bitwise_and(resized_8, resized_8, mask=mask_8)
        ##find contours in detected area
        image, contours, hierarchy= cv2.findContours(mask_8,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(contours))
        if len(contours)>0:
            stud_8=True
        else:
            stud_8=False
        #im= Image.fromarray(mask)
        #im.save("mask.jpg")
        #im2= Image.fromarray(croped)
        #im2.save("pink_filtered.jpg")

        ## Display
        #cv2.imshow("cropped_img8",crop_img8)
        #cv2.imshow("mask_8 ", mask_8)
        #cv2.imshow("croped", croped_8)


        #check stud status and show to user
        """print(stud_1)
        print(stud_2)
        print(stud_3)
        print(stud_4)
        print(stud_5)
        print(stud_6)
        print(stud_7)
        print(stud_8)"""
        
        if stud_1==True:
            outlined_image = cv2.rectangle(img, (535, 535), (585, 585), (0,255,0), 1)
            cv2.putText(outlined_image, 'Stud_1_OK', (535,605 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
            cv2.imshow("Result",outlined_image)
        else:
            outlined_image = cv2.rectangle(img, (535, 535), (585, 585), (0,0,255), 1)
            cv2.putText(outlined_image, 'Stud_1_NOK', (535,605 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow("Result",outlined_image)
            
            
            
        if stud_2==True:
                outlined_image = cv2.rectangle(img, (705, 520), (755, 570), (0,255,0), 1)
                cv2.putText(outlined_image, 'Stud_2_OK', (705,590 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
                cv2.imshow("Result",outlined_image)
        else:
                outlined_image = cv2.rectangle(img, (705, 520), (755, 570), (0,0,255), 1)
                cv2.putText(outlined_image, 'Stud_2_NOK', (705,590 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                cv2.imshow("Result",outlined_image)
                
                
        if stud_3==True:
            outlined_image = cv2.rectangle(img, (740, 320), (790, 370), (0,255,0), 1)
            cv2.putText(outlined_image, 'Stud_3_OK', (740,390 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
            cv2.imshow("Result",outlined_image)
        else:
            outlined_image = cv2.rectangle(img, (740, 320), (790, 370), (0,0,255), 1)
            cv2.putText(outlined_image, 'Stud_3_NOK', (740,390 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow("Result",outlined_image)
            
            
        if stud_4==True:
            outlined_image = cv2.rectangle(img, (700, 135), (750, 185), (0,255,0), 1)
            cv2.putText(outlined_image, 'Stud_4_OK', (700,205 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
            cv2.imshow("Result",outlined_image)
        else:
            outlined_image = cv2.rectangle(img, (700, 135), (750, 185), (0,0,255), 1)
            cv2.putText(outlined_image, 'Stud_4_NOK', (700,205 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow("Result",outlined_image)
        
        if stud_5==True:
            outlined_image = cv2.rectangle(img, (690, 70), (740, 120), (0,255,0), 1)
            cv2.putText(outlined_image, 'Stud_5_OK', (690,60 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
            cv2.imshow("Result",outlined_image)
        else:
            outlined_image = cv2.rectangle(img, (690, 70), (740, 120), (0,0,255), 1)
            cv2.putText(outlined_image, 'Stud_5_NOK', (690,60 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow("Result",outlined_image)
            
            
            
        if stud_6==True:
                outlined_image = cv2.rectangle(img, (280, 70), (330, 120), (0,255,0), 1)
                cv2.putText(outlined_image, 'Stud_6_OK', (280,140 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
                cv2.imshow("Result",outlined_image)
        else:
                outlined_image = cv2.rectangle(img, (280, 70), (330, 120), (0,0,255), 1)
                cv2.putText(outlined_image, 'Stud_6_NOK', (280,140 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                cv2.imshow("Result",outlined_image)
                
                
        if stud_7==True:
            outlined_image = cv2.rectangle(img, (190, 120), (240, 170), (0,255,0), 1)
            cv2.putText(outlined_image, 'Stud_7_OK', (190,190 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
            cv2.imshow("Result",outlined_image)
        else:
            outlined_image = cv2.rectangle(img, (190, 120), (240, 170), (0,0,255), 1)
            cv2.putText(outlined_image, 'Stud_7_NOK', (190,190 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow("Result",outlined_image)
            
            
        if stud_8==True:
            outlined_image = cv2.rectangle(img, (340, 360), (390, 410), (0,255,0), 1)
            cv2.putText(outlined_image, 'Stud_8_OK', (340,430 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
            cv2.imshow("Result",outlined_image)
        else:
            outlined_image = cv2.rectangle(img, (340, 360), (390, 410), (0,0,255), 1)
            cv2.putText(outlined_image, 'Stud_8_NOK', (340,430 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow("Result",outlined_image)
            
        if (stud_1,stud_2,stud_3,stud_4,stud_5,stud_6,stud_7,stud_8) ==True:
            io.do10=True #results are ok
            
        else:
            io.do10=False #results are nok
            
            cv2.waitKey(10)
            sleep(10)
            cv2.destroyAllWindows()
            
        



    

