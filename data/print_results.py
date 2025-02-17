#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Amita Kini Ravindra
# DATE CREATED:03.01.2025
# REVISED DATE: 04.01.2025
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
     # Prints summary statistics over the run
        #print(results_stats_dic)
        print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
        print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
        print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
        print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
   

    # Prints summary statistics (percentages) on Model Run
        print("\n\n*** Result summary in Percentage  for CNN Model Architecture",model.upper(), 
          "***")
    #for key in results_stats_dic:
        # the value is accessed 
        # by results_stats_dic[key]
        #    pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
        print("{:20}: {:3f} {:20}".format('Pct match', results_stats_dic['pct_match'],"%"))
        print("{:20}: {:3f} {:20}".format('Pct correct_dogs ', results_stats_dic['pct_correct_dogs'],"%"))
        print("{:20}: {:3f} {:20}".format('Pct correct_breed ', results_stats_dic['pct_correct_breed'],"%"))
        print("{:20}: {:3f} {:20}".format('Pct correct_notdogs', results_stats_dic['pct_correct_notdogs'],"%"))
        if print_incorrect_dogs is True:

         #calculate the incorrect dog calculation
         # to check if this exists add a conditiion correct_dogs+ correct_not dogs !=n_images
         # classifier says dog key[4]==1 and image says not dog key[3]==0  or vice versa 
         # in that case increement a counter and store the  the image file key and image name key[0] and classifier name key[1]
         # in a dict and print at the end with counter 
                if ( results_stats_dic['n_images']!=(results_stats_dic['n_correct_dogs']+results_stats_dic['n_correct_notdogs']))  :
                        counter_00=0
                        results_dic_anomaly =dict()
                        for key in results_dic:
                                if (sum (results_dic[key][3:]))==1:
                                        counter_00 +=1
                                        results_dic_anomaly[key]=[results_dic[key][0],results_dic[key][1]]
                        print ("{:20}: {:3d}".format('The number of incorrect dog calculation done by the model',counter_00))
                       
                        print("{:20}:".format('The images lables and corresponding classifier labels which were incorrectly calculated as dogs '))      
                       
                        for key in results_dic_anomaly:
                                print("{:20}:{:30}".format('images lables',results_dic_anomaly[key][0]))      
                                print("{:20}:{:30}".format('classifier lables',results_dic_anomaly[key][1]))      

        # calculate the incorrect breed 
        # breeds are incorrect  if correct_breed != correct_dogs 
        #breed is incorrect when classifier says dog key[4]==1 and image says dog key[3]==1 but pet label match is zero key[2]==0
 
         # in that case increement a counter and store the  the image file key and image name key[0] and classifier name key[1]
         # in a dict and print at the end with counter       
                        
        if print_incorrect_breed is True:

                if (results_stats_dic['n_correct_dogs']!=(results_stats_dic['n_correct_breed'])):
                        counter01=0
                        results_dic_anomaly_01 =dict()
                        for key in results_dic:
                                if results_dic[key][2]==0:
                                        if sum(results_dic[key][3:])==2:
                                                counter01 +=1
                                                results_dic_anomaly_01[key]=[results_dic[key][0],results_dic[key][1]]
                        print("{:20}: {:3d}".format('The number of incorrect dog breeds calculated by the model ',counter01 ))
                        print("{:20}:".format('The images lables and corresponding classifier labels which were incorrectly calculated dog breeds '))
                        for key in results_dic_anomaly_01:
                                print("{:20}: {:30}".format('images label ',results_dic_anomaly_01[key][0] ))
                                print("{:20}: {:30}".format('classifier labels',results_dic_anomaly_01[key][1] ))

                                
                



        """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    
                
