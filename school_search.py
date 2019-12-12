#!/usr/bin/env python3

import csv, time, itertools

# school_search.py


 
def search_schools(text_to_search):
    with open('sl051bai.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        schools = []
        cities = []
        states = []
      
        print(f"Results for '{text_to_search}':")
        text_to_search = text_to_search.upper()

        
        start_time = time.perf_counter()
        found = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lschool = row[3].upper()
                lcity = row[4].upper()
                lstate = row[5].upper()
            
                if lschool.count(text_to_search) > 0:
                    
                    found += 1
                    
                    schools.append(lschool)
                    cities.append(lcity)
                    states.append(lstate)
                    
                    if found == 3:
                        end_time = time.perf_counter()
                        print('(search took {0:.4f} seconds)'.format(round(end_time - start_time,4)))
                        for i in range(3):
                            sfound = str(i+1)
                            print(f'{sfound}. {schools[i]}, \n {cities[i]}, {states[i]}')        
                        break

                
        


    
         

