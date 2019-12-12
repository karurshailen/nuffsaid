#!/usr/bin/env python3

# count_schools.py

import csv, time, itertools

def print_counts():
    with open('sl051bai.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lcity05s = dict()
        lstate05s = dict()
        mlocales = dict()

        start_time = time.perf_counter()
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lcity = row[4]
                lstate = row[5]
            
                mlocale = row[8]
                if lcity in lcity05s:
                    lcity05s[lcity] += 1
                else:
                    lcity05s[lcity] = 0

                if lstate in lstate05s:
                    lstate05s[lstate] += 1
                else:
                    lstate05s[lstate] = 0
            
                if mlocale in mlocales:
                    mlocales[mlocale] += 1
                else:
                    mlocales[mlocale] = 0

                line_count += 1
        end_time = time.perf_counter()
    
        print(f'Total Schools: {line_count}')
    
        print(f'Schools by State:')
        count = 0
        for key in lstate05s:
            count += 1
            print(f'{str(count)}. {key} state has {lstate05s[key]} schools')
        count = 0
        for key in mlocales:
            count += 1
            print(f'{str(count)}. {key} mLocale has {mlocales[key]} schools')
        count = 0
        count_schools = 0
        one_school_min = 0
        max_schools = dict()
        for key in lcity05s:
            if lcity05s[key] > 0:
                count += 1
                if lcity05s[key] == 1:
                    one_school_min += 1
                print(f'{str(count)}. {key} city has {lcity05s[key]} schools')
                if count_schools <= int(lcity05s[key]):
                    count_schools = int(lcity05s[key])
                    max_schools = dict()
                    max_schools[key] = count_schools
            
        print(f'Max number of schools: {max_schools}')
        print(f'Number of unique cities with at least one school: {one_school_min}')
        print(f'Processing done in {end_time - start_time} seconds') 

