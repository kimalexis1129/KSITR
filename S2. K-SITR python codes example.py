#사례 파일 교체
casefile = open('C:/Users/SYK/Desktop/new case_0405_with tokens_to txt_encoding.txt','r', encoding = 'utf-8') 
#소스 북
srcfile = open('C:/Users/SYK/Desktop/new_group src book_0304_0311_0315(2)_encoding.txt','r', encoding = 'utf-8') 
results = open('C:/Users/SYK/Desktop/0406results/test1_results_0324.txt','w', encoding = 'utf-8') 

import sys
import os
import time
import re
import random
import re
case_cnt = 0
order_cnt = 0
G1_cnt = 0
G2_cnt = 0
G3_cnt = 0
G4_cnt = 0
G1_est = 0
G2_est = 0
G3_est = 0
G4_est = 0
flag = ""

while True:
    line = casefile.readline() #사례 읽기
    if not line: 
        break
    num = line.split("\t")[0]
    org_case = line.split("\t")[1].replace('"','') 
    case = line.split("\t")[2].replace("\n", "")
    if org_case.find("자살") != -1:
        #print(" ~~ flag??")
        #print(org_case)
        flag = "자살위험" #사례에 “자살”이 언급된 경우 주의 플래그(flag)
    else:
        flag = "none"
    if org_case.find("우울") != -1: 
        DEP_counter = org_case.count("우울")
        DEP_counter = int(DEP_counter)
    else:
        DEP_counter = 0
    if org_case.find("불안") != -1: 
        ANX_counter = org_case.count("불안")
        ANX_counter = int(ANX_counter)
    else:
        ANX_counter = 0
    while True:
        book = srcfile.readline() #토큰북 한줄씩 읽어오기
        #소스 북을 열어서 사례에서 도출된 어근들과 비교 
        if not book:
            break  
        group = book.split("\t")[0]
        tok = book.split("\t")[1]
        tok_value = book.split("\t")[4] 
        if case.find(tok) != -1:  #사례에서 소스 북 특정 어근이 발견된 경우
            tok_counter = case.count(tok) 
            group = int(group)
            tok_value = int(tok_value) #어근의 대표성 값 
            tok_counter = int(tok_counter)  #사례 내 해당 어근의 개수

            if group == 1:
                G1_est = G1_est + (tok_value*tok_counter)
                if str(tok) == "우울증" or "커터_칼" or "커터칼" or "트라우마" or "인격장애" or "경계성_인격장애" or "성격장애": #메타분석 결과, 자살 위험을 높이는 고위험 특징어 가중
                    G1_est += 1
                if order_cnt < 3: #사례에서 먼저 도출된 3개 어근에 (순서)가중
                    G1_est += 1 
                G1_cnt += 1 
            elif group == 2:
                G2_est = G2_est + (tok_value*tok_counter)
                if str(tok) == "우울증" or "커터_칼" or "커터칼" or "트라우마" or "인격장애" or "경계성_인격장애" or "성격장애":
                    G2_est += 1
                if order_cnt < 3:
                    G2_est += 1 
                G2_cnt += 1 
            elif group == 3:
                G3_est = G3_est + (tok_value*tok_counter)
                if str(tok) == "우울증" or "커터_칼" or "커터칼" or "트라우마" or "인격장애" or "경계성_인격장애" or "성격장애":
                    G3_est += 1
                if order_cnt < 3:
                    G3_est += 1 
                G3_cnt += 1 
            else:
                G4_est = G4_est + (tok_value*tok_counter)
                if str(tok) == "우울증" or "커터_칼" or "커터칼" or "트라우마" or "인격장애" or "경계성_인격장애" or "성격장애":
                    G4_est += 1
                if order_cnt < 3:
                    G4_est += 1 
                G4_cnt += 1
            order_cnt += 1
        else:
            pass
    case_cnt += 1 
    srcfile.close()
    srcfile = open('C:/Users/SYK/Desktop/new_group src book_0304_0311_0315(2)_encoding.txt','r', encoding = 'utf-8') 
    results.write(str(case_cnt) + "\t" + org_case + "\t" + case + "\t" +
                  str(G1_cnt) + "\t" + str(G1_est) + "\t" + str(G2_cnt) + "\t" + str(G2_est) + "\t" +
                  str(G3_cnt) + "\t" + str(G3_est) + "\t" + str(G4_cnt) + "\t" + str(G4_est) + "\t" +
                  flag + "\t" + str(DEP_counter) + "\t" + str(ANX_counter) + "\n") 
        
    order_cnt = 0
    G1_cnt = 0
    G2_cnt = 0
    G3_cnt = 0
    G4_cnt = 0
    G1_est = 0
    G2_est = 0
    G3_est = 0
    G4_est = 0
  
casefile.close()
srcfile.close()
results.close() #소스 북과 비교하여 사례 내 자료집단별 대표성 값 계산 결과 저장

inputformatch = open('C:/Users/SYK/Desktop/0406results/test1_results_0324.txt','r', encoding = 'utf-8') 
results2 = open('C:/Users/SYK/Desktop/0406results/test2_results_matching_0324.txt','w', encoding = 'utf-8') 
error = open('C:/Users/SYK/Desktop/0406results/test2_results_error_0324.txt','w', encoding = 'utf-8') #WRITE
dup = open('C:/Users/SYK/Desktop/0406results/test2_results_duplicates_0324.txt','w', encoding = 'utf-8') #WRITE
matching_cnt = 1 

while True:
    line2 = inputformatch.readline() #대표성 값 계산 결과 읽기 
    if not line2: 
        break
    num = line2.split("\t")[0]
    org_case = line2.split("\t")[1]
    case = line2.split("\t")[2]
    G1_cnt = line2.split("\t")[3]
    G1_est = line2.split("\t")[4]
    G2_cnt = line2.split("\t")[5]
    G2_est = line2.split("\t")[6]
    G3_cnt = line2.split("\t")[7]
    G3_est = line2.split("\t")[8]
    G4_cnt = line2.split("\t")[9]
    G4_est = line2.split("\t")[10]
    flag = line2.split("\t")[11] 
    DEP_counter = line2.split("\t")[12]
    ANX_counter = line2.split("\t")[13].replace("\n", "") 
    G1_est = int(G1_est) 
    G2_est = int(G2_est)
    G3_est = int(G3_est)
    G4_est = int(G4_est)
    G1_cnt = int(G1_cnt)
    G2_cnt = int(G2_cnt)
    G3_cnt = int(G3_cnt)
    G4_cnt = int(G4_cnt)
    estimated_group = 0
    G_est = [G1_est, G2_est, G3_est, G4_est] #자료집단 별 대표성 계산 값 비교 
    max_est = max(G_est) #가장 높은 대표성 값을 가진 자료집단 확인
    G_cnt = [G1_cnt, G2_cnt, G3_cnt, G4_cnt]

    if(len(G_est) != len(set(G_est)) and len(G_cnt) != len(set(G_cnt))): 
        duplicate_element = set([x for x in G_est if G_est.count(x) > 1])
        duplicate_element = str(duplicate_element).replace("{","").replace("}","") 
        if (str(duplicate_element).find(", ") != -1):
            first_duplicate_element = duplicate_element.split(", ")[0]
            second_duplicate_element = duplicate_element.split(", ")[1]
            int(second_duplicate_element))
        duplicate_element2 = set([x for x in G_cnt if G_cnt.count(x) > 1])
        duplicate_element2 = str(duplicate_element2).replace("{","").replace("}","") 
        if (str(duplicate_element2).find(", ") != -1): 
            first_duplicate_element2 = duplicate_element2.split(", ")[0]
            second_duplicate_element2 = duplicate_element2.split(", ")[1]
            duplicate_element2 = max(int(first_duplicate_element2), int(second_duplicate_element2))
        print("Case < " + str(matching_cnt) + " > has a duplicate element...") 
        print(" => tok_importance duplicate:: " + str(duplicate_element))
        print(" => tok match freq duplicate:: " + str(duplicate_element2))
        print("[G1,  G2,  G3,  G4]") #자료집단 2개 이상에 해당되는 경우, 해당 데이터 확인
        print(str(G_est).replace("'",""))
        print("[G1,  G2,  G3,  G4]")
        print(str(G_cnt).replace("'",""))
        duplicate_element = int(duplicate_element)
        duplicate_element2 = int(duplicate_element2)
        max_est = int(max_est)
        max_cnt = int(max_cnt)
        if duplicate_element == max_est and duplicate_element2 == max_cnt:
            est_condition = ','.join(str(e) for e in G_est) 
            est_condition = str(est_condition.replace("\n",""))
            est_condition_len = len(est_condition)
            est_condition_len_slice = est_condition_len//4 
            est_target = str(duplicate_element) #중복된 값 찾기 
            est_loc = est_condition.find(est_target) 
            est_loc2 = est_condition.rfind(est_target) 
            if est_loc < est_condition_len_slice:
                est_loc_found = 1 #'group1'
            elif est_loc < est_condition_len_slice*2:
                est_loc_found = 2 #'group2'
            elif est_loc > est_condition_len_slice*2:
                est_loc_found = 3 #'group3'
            else:
                print("CANNOT examine this case! need human judgement!") #세부 대표성 값을 비교해도 가장 걸맞은 자료집단을 고르기 어려운 경우, ‘전문가가 직접 검토해야 할 사례’로 분류하고 error 파일로 저장 
            if est_loc2 > est_condition_len_slice*3:
                est_loc2_found = 4 #'group4'
            elif est_loc2 > est_condition_len_slice*2:
                est_loc2_found = 3 #'group3'
            elif est_loc2 < est_condition_len_slice*2:
                est_loc2_found = 2 #'group2' 
            else:
                print("CANNOT examine this case! need human judgement!")
            if flag == "자살위험": 
                print(" ~~ this case might imply suicidal thoughts! ... putting this case into GROUP 2") 
                sug_group = 2
            elif est_loc_found == 3 or est_loc2_found == 3:
                sug_group = 3
            else:
                sug_group = "NONE" 
            dup.write(str(matching_cnt) + "\t" + line2.replace("\n","") + "\t" + str(est_loc_found) + "\t" + str(est_loc2_found) + "\t" + str(sug_group) + "\n")
            results2.write(str(matching_cnt) + "\t" + line2.replace("\n", "") + "\t" + str(sug_group) + "\n")   #"\t" + "**check this case" + "\n")
        elif duplicate_element == max_est: #and (duplicate_element2 != max_cnt):
            #print("One duplicate element exists!")
            if max_cnt == G1_cnt : #세부 대표성 값을 이용하면 가장 걸맞은 자료집단 선택이 가능한 경우 
                estimated_group = 1
            elif max_cnt == G2_cnt :
                estimated_group = 2
            elif max_cnt == G3_cnt :
                estimated_group = 3
            elif max_cnt == G4_cnt:
                estimated_group = 4
            else:
            print("using freq. instead, resulted in group < " + str(estimated_group) + " >")
            results2.write(str(matching_cnt) + "\t" + line2.replace("\n", "") + "\t" + str(estimated_group) + "\n") 
            if max_est == G1_est:
                estimated_group = 1
            elif max_est == G2_est :
                estimated_group = 2
            elif max_est == G3_est :
                estimated_group = 3
            elif max_est == G4_est :
                estimated_group = 4
            else:
                print("CANNOT examine this case! need human judgement!")
            results2.write(str(matching_cnt) + "\t" + line2.replace("\n", "") + "\t" + str(estimated_group) + "\n") 
        else:
            print("still something else?")
            #os.system("Pause") 
            print() 
            error.write(str(matching_cnt) + "\t" + line2) 
    else:
        if max_est == G1_est:
            estimated_group = 1
        elif max_est == G2_est :
            estimated_group = 2
        elif max_est == G3_est :
            estimated_group = 3
        elif max_est == G4_est :
            estimated_group = 4
        else :
            print("still something, another else?")
            error.write(str(matching_cnt) + "\t" + line2)
        results2.write(str(matching_cnt) + "\t" + line2.replace("\n", "") + "\t" + str(estimated_group) + "\n")  
#사례에 맞는 자료집단 결정 결과 저장 
    estimated_group = 0 
    sug_group = 0
    matching_cnt += 1
inputformatch.close()
results2.close()
error.close()
dup.close()

grouped_case = open('C:/Users/SYK/Desktop/0406results/test2_results_matching_0324.txt','r', encoding = 'utf-8') 
results3 = open('C:/Users/SYK/Desktop/0406results/test3_results_topic match_0324.txt','w', encoding = 'utf-8')
error3 = open('C:/Users/SYK/Desktop/0406results/test3_results_error_0324.txt','w', encoding = 'utf-8') 

topic_match_cnt = 1 
topic_profile = ""
t0_cnt = 0
t1_cnt = 0
t2_cnt = 0
t3_cnt = 0
t4_cnt = 0
t5_cnt = 0
t6_cnt = 0
t7_cnt = 0
t8_cnt = 0
t9_cnt = 0
t0_est = 0
t1_est = 0
t2_est = 0
t3_est = 0
t4_est = 0
t5_est = 0
t6_est = 0
t7_est = 0
t8_est = 0
t9_est = 0

while True: #자료집단이 결정된 사례 다시 읽기 
    line3 = grouped_case.readline()
    print()
    if not line3:
        break
    num = line3.split("\t")[1]
    org_case = line3.split("\t")[2]
    case = line3.split("\t")[3]
    G1_cnt = line3.split("\t")[4]
    G1_est = line3.split("\t")[5]
    G2_cnt = line3.split("\t")[6]
    G2_est = line3.split("\t")[7]
    G3_cnt = line3.split("\t")[8]
    G3_est = line3.split("\t")[9]
    G4_cnt = line3.split("\t")[10]
    G4_est = line3.split("\t")[11]
    flag = line3.split("\t")[12] 
    DEP_counter = line3.split("\t")[13] 
    ANX_counter = line3.split("\t")[14]
    M_group = line3.split("\t")[15].replace("\n", "")
    if str(M_group) == "NONE":
        print("this case needs human judgement!")
        error3.write(line3)

    #1번 자료집단으로 분류된 사례는 자료집단의 토픽모델과 비교, 점유율 계산 시작
    elif int(M_group) == 1:
        G1_src = open('C:/Users/SYK/Desktop/group_src books_0315/G1_srcbook_0315.txt','r', encoding = 'utf-8')
        while True:
            G1_book = G1_src.readline()
            if not G1_book:
                break
            tok = G1_book.split("\t")[1]
            tok_value = G1_book.split("\t")[4]
            topic_num = G1_book.split("\t")[5]
            topic_title = G1_book.split("\t")[6]
            topic_val = G1_book.split("\t")[8].replace("\n", "")
            topic_num = int(topic_num)
            topic_val = int(topic_val)
            if case.find(tok) != -1: 
                tok_counter = case.count(tok) 
                if topic_num == 0:
                    t0_est += (topic_val*tok_counter) 
                    t0_cnt += 1
                elif topic_num == 1:
                    t1_est += (topic_val*tok_counter)
                    t1_cnt += 1
                elif topic_num == 2:
                    t2_est += (topic_val*tok_counter)
                    t2_cnt += 1
                elif topic_num == 3:
                    t3_est += (topic_val*tok_counter)
                    t3_cnt += 1
                elif topic_num == 4:
                    t4_est += (topic_val*tok_counter)
                    t4_cnt += 1
                elif topic_num == 5:
                    t5_est += (topic_val*tok_counter)
                    t5_cnt += 1
                elif topic_num == 6:
                    t6_est += (topic_val*tok_counter)
                    t6_cnt += 1
                elif topic_num == 7:
                    t7_est += (topic_val*tok_counter)
                    t7_cnt += 1
                elif topic_num == 8:
                    t8_est += (topic_val*tok_counter)
                    t8_cnt += 1
                elif topic_num == 9:
                    t9_est += (topic_val*tok_counter)
                    t9_cnt += 1 
                else:
                    pass
            topic_profile = (str(t0_cnt) + "\t" + str(t0_est) + "\t" + str(t1_cnt) + "\t" + str(t1_est) + "\t" +
                             str(t2_cnt) + "\t" + str(t2_est) + "\t" + str(t3_cnt) + "\t" + str(t3_est) + "\t" +
                             str(t4_cnt) + "\t" + str(t4_est) + "\t" + str(t5_cnt) + "\t" + str(t5_est) + "\t" +
                             str(t6_cnt) + "\t" + str(t6_est) + "\t" + str(t7_cnt) + "\t" + str(t7_est) + "\t" +
                             str(t8_cnt) + "\t" + str(t8_est) + "\t" + str(t9_cnt) + "\t" + str(t9_est)) #사례 내 토픽 프로파일 계산 
        G1_src.close()

    else: 
        print(M_group)
        print("this case requires human judgement!")
        error3.write(line3)
    results3.write(line3.replace("\n", "") + "\t" + topic_profile + "\t") #사례의 토픽 프로파일 계산 결과 저장 

    #사례의 토픽 프로파일 점유율 내림차순 정렬
    topic_est_dic = {}
    topic_cnt_dic = {}
    topic_est_dic = {"topic0" : t0_est, "topic1" : t1_est, "topic2" : t2_est, "topic3" : t3_est,
                     "topic4" : t4_est, "topic5" : t5_est, "topic6" : t6_est, "topic7" : t7_est,
                     "topic8" : t8_est, "topic9" : t9_est }
    sorted_topic_est_dic = sorted(topic_est_dic.items(), key = lambda x: x[1], reverse = True) 
    topic_cnt_dic = {"topic0" : t0_cnt, "topic1" : t1_cnt, "topic2" : t2_cnt, "topic3" : t3_cnt,
                     "topic4" : t4_cnt, "topic5" : t5_cnt, "topic6" : t6_cnt, "topic7" : t7_cnt,
                     "topic8" : t8_cnt, "topic9" : t9_cnt }
    sorted_topic_cnt_dic = sorted(topic_cnt_dic.items(), key = lambda x: x[1], reverse = True) 
    results3.write(str(sorted_topic_est_dic).replace("[","").replace("('","").replace("', ","=").replace("),",";").replace("]","").replace(")","")
                   + "\t" + str(sorted_topic_cnt_dic).replace("[","").replace("('","").replace("', ","=").replace("),",";").replace("]","").replace(")","") + "\n") #정렬된 프로파일 저장
    topic_match_cnt += 1  
    t0_cnt = 0 
    t1_cnt = 0
    t2_cnt = 0
    t3_cnt = 0
    t4_cnt = 0
    t5_cnt = 0
    t6_cnt = 0
    t7_cnt = 0
    t8_cnt = 0
    t9_cnt = 0
    t0_est = 0
    t1_est = 0
    t2_est = 0
    t3_est = 0
    t4_est = 0
    t5_est = 0
    t6_est = 0
    t7_est = 0
    t8_est = 0
    t9_est = 0

grouped_case.close()
results3.close()
error3.close()

pfmatch_case = open('C:/Users/SYK/Desktop/0406results/test3_results_topic match_0324.txt','r', encoding = 'utf-8')
results4 = open('C:/Users/SYK/Desktop/0406results/disser_test4_results_ranks_0324.txt','w', encoding = 'utf-8') 
error4 = open('C:/Users/SYK/Desktop/0406results/disser_test4_results_error_0324.txt','w', encoding = 'utf-8') 
case_human = "" 
case_CBT = ""
case_DBT = ""
case_ACT = ""
case_G_T = ""
case_trait = ""
case_emo = ""
case_idea = ""
case_past = ""
case_present = ""
rank_match_cnt = 1 

while True:
    line4 = pfmatch_case.readline() #사례의 프로파일 외 모든 계산 결과 읽기 
    if not line4:
        break
    num = line4.split("\t")[0]
    org_case = line4.split("\t")[2]
    ind_case = line4.split("\t")[3]
    flag = line4.split("\t")[12] 
    DEP_counter = line4.split("\t")[13] 
    ANX_counter = line4.split("\t")[14]
    group = line4.split("\t")[15]
    T0_est = line4.split("\t")[17]
    T1_est = line4.split("\t")[19]
    T2_est = line4.split("\t")[21]
    T3_est = line4.split("\t")[23]
    T4_est = line4.split("\t")[25]
    T5_est = line4.split("\t")[27]
    T6_est = line4.split("\t")[29]
    T7_est = line4.split("\t")[31]
    T8_est = line4.split("\t")[33]
    T9_est = line4.split("\t")[35]
    case_profile = line4.split("\t")[36]
    case_profile_sub = line4.split("\t")[37].replace("\n","")
    case_profile_dic = {}
    case_profile_dic = {"topic0" : T0_est, "topic1" : T1_est, "topic2" : T2_est, "topic3" : T3_est,
                        "topic4" : T4_est, "topic5" : T5_est, "topic6" : T6_est, "topic7" : T7_est,
                        "topic8" : T8_est, "topic9" : T9_est }
    if str(group) == "NONE" :
        error4.write(line4)
        os.system("Pause")
        pass
    
    #1번 자료집단의 사례라면, 해당 자료집단 내 트레이닝 데이터 프로파일들과 비교 
    elif int(group) == 1 :
        group = int(group)
        G1_profile_book = open('C:/Users/SYK/Desktop/group_src books_0315/GROUP1 topic profile manual book_0316_to txt.txt','r', encoding = 'utf-8')
        while True:
            G1_manual = G1_profile_book.readline()
            if not G1_manual:
                break
            manual_id = G1_manual.split("\t")[0]
            manual_T0_est = G1_manual.split("\t")[1]
            manual_T1_est = G1_manual.split("\t")[2]
            manual_T2_est = G1_manual.split("\t")[3]
            manual_T3_est = G1_manual.split("\t")[4]
            manual_T4_est = G1_manual.split("\t")[5]
            manual_T5_est = G1_manual.split("\t")[6]
            manual_T6_est = G1_manual.split("\t")[7]
            manual_T7_est = G1_manual.split("\t")[8]
            manual_T8_est = G1_manual.split("\t")[9]
            manual_T9_est = G1_manual.split("\t")[10]
            manual_profile = G1_manual.split("\t")[11]
            manual_profile_sub = G1_manual.split("\t")[12]
            human = G1_manual.split("\t")[13]
            CBT = G1_manual.split("\t")[14]
            DBT = G1_manual.split("\t")[15]
            ACT = G1_manual.split("\t")[16]
            G_T = G1_manual.split("\t")[17]
            trait = G1_manual.split("\t")[18]
            emo = G1_manual.split("\t")[19]
            idea = G1_manual.split("\t")[20]
            past = G1_manual.split("\t")[21]
            present = G1_manual.split("\t")[22].replace("\n","")
            manual_dic = {}
            manual_dic = {"topic0" : manual_T0_est, "topic1" : manual_T1_est, "topic2" : manual_T2_est, "topic3" : manual_T3_est,
                          "topic4" : manual_T4_est, "topic5" : manual_T5_est, "topic6" : manual_T6_est, "topic7" : manual_T7_est,
                          "topic8" : manual_T8_est, "topic9" : manual_T9_est }
            case_profile_dic_len = len(case_profile_dic)
            manual_dic_len = len(manual_dic)
            total_dic_count = case_profile_dic_len + manual_dic_len
            shared_dic = {} #사례 프로파일과 트레이닝 데이터 프로파일들 간 유사도 비교
            for i in manual_dic:
                if (i in case_profile_dic) and (manual_dic[i] == case_profile_dic[i]):
                    shared_dic[i] = manual_dic[i]
            len_shared_dic = len(shared_dic)
            if (len_shared_dic == total_dic_count//2): #프로파일이 일치하는 경우
                case_human = human #해당 트레이닝 데이터에 부여되었던 상담 전문가의 순위형 평가 값(추천 상담 접근방법 및 개입 시 우선순위) 불러오기 
                case_CBT = CBT
                case_DBT = DBT
                case_ACT = ACT
                case_G_T = G_T
                case_trait = trait
                case_emo = emo
                case_idea = idea
                case_past = past
                case_present = present
                break
            elif (len_shared_dic >= 9):  #사례의 프로파일과 완벽하게 일치하는 트레이닝 데이터가 없다면, 요소들이 9개 이상(프로파일 내 점유율 유효 값(“0”이 아닌 값) 항목 및 내림차순 정렬 시 순서) 일치해서 유사도가 가장 높은 트레이닝 데이터 찾기
                case_human = human
                case_CBT = CBT
                case_DBT = DBT
                case_ACT = ACT
                case_G_T = G_T
                case_trait = trait
                case_emo = emo
                case_idea = idea
                case_past = past
                case_present = present
            else:
                pass
        treatment = {}
        treatment = {"humanistic" : case_human, "B-CBT" : case_CBT, "DBT" : case_DBT, "ACT" : case_ACT, "group_training" : case_G_T }
        sorted_treatment = sorted(treatment.items(), key = lambda x: x[1], reverse = True) 
        inter_target = {}
        inter_target = {"trait" : case_trait, "emotion" : case_emo, "thoughts" : case_idea, "past exp." : case_past, "present exp." : case_present }
        sorted_inter_target = sorted(inter_target.items(), key = lambda x: x[1], reverse = True)
        report = (str(case_human) + "\t" + str(case_CBT) + "\t" + str(case_DBT) + "\t" +
                  str(case_ACT) + "\t" + str(case_G_T) + "\t" + str(case_trait) + "\t" +
                  str(case_emo) + "\t" + str(case_idea) + "\t" + str(case_past) + "\t" + str(case_present) )
        results4.write(line4.replace("\n","") + "\t" + report + "\t" + str(sorted_treatment).replace("[","").replace("('","").replace("', ","=").replace("),",";").replace("]","").replace(")","").replace("'","")
                       + "\t" + str(sorted_inter_target).replace("[","").replace("('","").replace("', ","=").replace("),",";").replace("]","").replace(")","").replace("'","") + "\n")
        rank_match_cnt += 1
        
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt #검사 결과 시각화를 위한 matplotlib 모듈 불러오기 
import platform
if platform.system() == 'Darwin': 
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': 
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': 
        plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False 
from wordcloud import WordCloud
from collections import Counter
import fpdf #결과 보고서 자동 구성 및 출력을 위한 FPDF 모듈 불러오기
from fpdf import FPDF
import time
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi

computer_results = open('C:/Users/SYK/Desktop/0406results/disser_test4_results_ranks_0324.txt','r', encoding = 'utf-8') #READ cases w. group
results5 = open('C:/Users/SYK/Desktop/0406results/TRANS_test5_results_topic match_0324_test.txt','w', encoding = 'utf-8') #보고서에 포함할 모든 사례 평가결과 불러오기 
error5 = open('C:/Users/SYK/Desktop/0406results/TRANS_test5_results_error_0324_test.txt','w', encoding = 'utf-8')
trans_case = 1 
while True:
    line5 = computer_results.readline()
    if not line5:
        break
    num = line5.split("\t")[0]
    org_case = line5.split("\t")[2]
    token_case = line5.split("\t")[3]
    flag = line5.split("\t")[12] #flag 신규 추가
    DEP_counter = line5.split("\t")[13] #우울&불안 언급 카운터 신규 추가
    ANX_counter = line5.split("\t")[14]
    group = line5.split("\t")[15]
    t0_cnt = line5.split("\t")[16]
    t0_est = line5.split("\t")[17]
    t1_cnt = line5.split("\t")[18]
    t1_est = line5.split("\t")[19]
    t2_cnt = line5.split("\t")[20]
    t2_est = line5.split("\t")[21]
    t3_cnt = line5.split("\t")[22]
    t3_est = line5.split("\t")[23]
    t4_cnt = line5.split("\t")[24]
    t4_est = line5.split("\t")[25]
    t5_cnt = line5.split("\t")[26]
    t5_est = line5.split("\t")[27]
    t6_cnt = line5.split("\t")[28]
    t6_est = line5.split("\t")[29]
    t7_cnt = line5.split("\t")[30]
    t7_est = line5.split("\t")[31]
    t8_cnt = line5.split("\t")[32]
    t8_est = line5.split("\t")[33]
    t9_cnt = line5.split("\t")[34]
    t9_est = line5.split("\t")[35] 
    topic_profile_est = line5.split("\t")[36]
    topic_profile_cnt = line5.split("\t")[37]
    human = line5.split("\t")[38]
    B_CBT = line5.split("\t")[39]
    DBT = line5.split("\t")[40]
    ACT = line5.split("\t")[41]
    G_T = line5.split("\t")[42]
    trait = line5.split("\t")[43]
    emo = line5.split("\t")[44]
    cog = line5.split("\t")[45]
    past = line5.split("\t")[46]
    present = line5.split("\t")[47]
    treatment_rank = line5.split("\t")[48]
    inter_target_rank = line5.split("\t")[49].replace("\n","")
    DEP_counter = int(DEP_counter)
    ANX_counter = int(ANX_counter)
    group_trans = ""
    topic_profile_trans = "“

    if int(group) == 1: #자료집단별 결과와 걸맞은 해설 매치(match) 시키기 
        group_trans = "이 사례는 <비교적 어려운 상담이 예상되는 심각한 사례이지만, 상담 예후가 준수할/좋을 가능성이 있는> 사례입니다."
        if flag == "자살위험": #사례에 “자살” 언급이 있었던 경우, 주의 문구 포함하기 
            flag_trans = "<자살> 생각이 있을 위험이 엿보이므로, 상담 시 자살 관련 생각과 계획 유무, 위험수준을 최우선순위로 확인해주십시오. 다음으로, 사례에서 발견된 내담자의 키워드(특징어) 등을 참고하셔서 상담 준비에 활용하시기 바랍니다."
        else:
            flag_trans = "다음으로, 사례에서 발견된 내담자의 키워드(특징어) 등을 참고하셔서 상담 준비에 활용하시기 바랍니다."
        topic_name_0 = topic_profile_est.split("=")[0]
        topic_name_1 = topic_profile_est.split("=")[1].split("; ")[1]
        topic_name_2 = topic_profile_est.split("=")[2].split("; ")[1]
        topic_name_3 = topic_profile_est.split("=")[3].split("; ")[1]
        topic_name_4 = topic_profile_est.split("=")[4].split("; ")[1]
        topic_name_5 = topic_profile_est.split("=")[5].split("; ")[1]
        topic_name_6 = topic_profile_est.split("=")[6].split("; ")[1]
        topic_name_7 = topic_profile_est.split("=")[7].split("; ")[1]
        topic_name_8 = topic_profile_est.split("=")[8].split("; ")[1]
        topic_name_9 = topic_profile_est.split("=")[9].split("; ")[1]
        topic_est_0 = topic_profile_est.split("=")[1].split("; ")[0]
        topic_est_1 = topic_profile_est.split("=")[2].split("; ")[0]
        topic_est_2 = topic_profile_est.split("=")[3].split("; ")[0]
        topic_est_3 = topic_profile_est.split("=")[4].split("; ")[0]
        topic_est_4 = topic_profile_est.split("=")[5].split("; ")[0]
        topic_est_5 = topic_profile_est.split("=")[6].split("; ")[0]
        topic_est_6 = topic_profile_est.split("=")[7].split("; ")[0]
        topic_est_7 = topic_profile_est.split("=")[8].split("; ")[0]
        topic_est_8 = topic_profile_est.split("=")[9].split("; ")[0]
        topic_est_9 = topic_profile_est.split("=")[10] #.split("; ")[0]
        topic_est_0 = int(topic_est_0)
        topic_est_1 = int(topic_est_1)
        topic_est_2 = int(topic_est_2)
        topic_est_3 = int(topic_est_3)
        topic_est_4 = int(topic_est_4)
        topic_est_5 = int(topic_est_5)
        topic_est_6 = int(topic_est_6)
        topic_est_7 = int(topic_est_7)
        topic_est_8 = int(topic_est_8)
        topic_est_9 = int(topic_est_9)

	#토픽 색인 번호를 해당 토픽 명칭과 매치 시키기 
        topic_name_0 = topic_name_0.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_1 = topic_name_1.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_2 = topic_name_2.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_3 = topic_name_3.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_4 = topic_name_4.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_5 = topic_name_5.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_6 = topic_name_6.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_7 = topic_name_7.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_8 = topic_name_8.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_name_9 = topic_name_9.replace("topic0", "자기 비난").replace("topic1", "청소년기 학교생활 부적응").replace("topic2", "학교폭력 관련 경험").replace("topic3", "청소년기 심리문제").replace("topic4", "가정 내 부적절한 통제).replace("topic5", "청소년기 학교생활 부적응(보다 세부적인 문제)").replace("topic6", "가정 내 마찰(보다 세부적인 문제)").replace("topic7", "청소년기 학교생활 부적응(보다 더 세부적인 문제)").replace("topic8", "가정 내 지지 부족").replace("topic9", "또래관계 문제")
        topic_sec_0 = topic_profile_est.split("=")[1].split(";")[0]
        if int(topic_sec_0) == 0:
            topic_name_0 = "none"
            topic_sec_0_def = "none" 
            #topic_sec_0_def = "발견되지 않았습니다."
        else:
            topic_sec_0_def = "이/가 가장 두드러진 주제로 나타납니다. 그 다음으로 사례에서 발견된 주제들(중요도순)은 다음과 같습니다: "
        topic_sec_1 = topic_profile_est.split("=")[2].split(";")[0]
        if int(topic_sec_1) == 0:
            topic_name_1 = "none"
            topic_sec_1_def = "none"
            #topic_sec_1_def = "발견되지 않았습니다."
        else:
            topic_sec_1_def = ". "
        topic_sec_2 = topic_profile_est.split("=")[3].split(";")[0]
        if int(topic_sec_2) == 0:
            topic_name_2 = "none"
            topic_sec_2_def = "none" 
        else:
            topic_sec_2_def = ". "
        topic_sec_3 = topic_profile_est.split("=")[4].split(";")[0]
        if int(topic_sec_3) == 0:
            topic_name_3 = "none"
            topic_sec_3_def = "none" 
        else:
            topic_sec_3_def = ". "
        topic_sec_4 = topic_profile_est.split("=")[5].split(";")[0]
        if int(topic_sec_4) == 0:
            topic_name_4 = "none"
            topic_sec_4_def = "none"
        else:
            topic_sec_4_def = ". "
        topic_sec_5 = topic_profile_est.split("=")[6].split(";")[0]
        if int(topic_sec_5) == 0:
            topic_name_5 = "none"
            topic_sec_5_def = "none" 
        else:
            topic_sec_5_def = ". "
        topic_sec_6 = topic_profile_est.split("=")[7].split(";")[0]
        if int(topic_sec_6) == 0:
            topic_name_6 = "none"
            topic_sec_6_def = "none" 
        else:
            topic_sec_6_def = ". "
        topic_sec_7 = topic_profile_est.split("=")[8].split(";")[0]
        if int(topic_sec_7) == 0:
            topic_name_7 = "none"
            topic_sec_7_def = "none" 
        else:
            topic_sec_7_def = ". "
        topic_sec_8 = topic_profile_est.split("=")[9].split(";")[0]
        if int(topic_sec_8) == 0:
            topic_name_8 = "none"
            topic_sec_8_def = "none" 
        else:
            topic_sec_8_def = ". "
        topic_sec_9 = topic_profile_est.split("=")[10] #.split(";")[0]
        if int(topic_sec_9) == 0:
            topic_name_9 = "none"
            topic_sec_9_def = "none" 
        else:
            topic_sec_9_def = "."
        topic_profile_trans = ("이 사례에서 추정되는 호소주제들입니다. 먼저, "
                               + topic_name_0 + topic_sec_0_def
                               + topic_name_1 + topic_sec_1_def
                               + topic_name_2 + topic_sec_2_def
                               + topic_name_3 + topic_sec_3_def
                               + topic_name_4 + topic_sec_4_def
                               + topic_name_5 + topic_sec_5_def
                               + topic_name_6 + topic_sec_6_def
                               + topic_name_7 + topic_sec_7_def
                               + topic_name_8 + topic_sec_8_def
                               + topic_name_9 + topic_sec_9_def )
        topic_profile_trans = topic_profile_trans.replace("none", "")
        treat_1 = treatment_rank.split("=")[0]
        treat_2 = treatment_rank.split("=")[1].split("; ")[1]
        treat_3 = treatment_rank.split("=")[2].split("; ")[1]
        treat_4 = treatment_rank.split("=")[3].split("; ")[1]
        treat_5 = treatment_rank.split("=")[4].split("; ")[1]

	#내림차순 정렬된 순서대로 해당 상담 접근방법(이름) 불러오기 
        treat_1 = treat_1.replace("humanistic", "인간중심").replace("B-CBT", "단기 인지행동치료(CBT)").replace("DBT", "변증법적 행동치료(DBT)").replace("ACT", "수용전념치료(ACT)").replace("group_training", "기술훈련 집단(정서조절, 의사소통 기술 등)")
        treat_2 = treat_2.replace("humanistic", "인간중심").replace("B-CBT", "단기 인지행동치료(CBT)").replace("DBT", "변증법적 행동치료(DBT)").replace("ACT", "수용전념치료(ACT)").replace("group_training", "기술훈련 집단(정서조절, 의사소통 기술 등)")
        treat_3 = treat_3.replace("humanistic", "인간중심").replace("B-CBT", "단기 인지행동치료(CBT)").replace("DBT", "변증법적 행동치료(DBT)").replace("ACT", "수용전념치료(ACT)").replace("group_training", "기술훈련 집단(정서조절, 의사소통 기술 등)")
        treat_4 = treat_4.replace("humanistic", "인간중심").replace("B-CBT", "단기 인지행동치료(CBT)").replace("DBT", "변증법적 행동치료(DBT)").replace("ACT", "수용전념치료(ACT)").replace("group_training", "기술훈련 집단(정서조절, 의사소통 기술 등)")
        treat_5 = treat_5.replace("humanistic", "인간중심").replace("B-CBT", "단기 인지행동치료(CBT)").replace("DBT", "변증법적 행동치료(DBT)").replace("ACT", "수용전념치료(ACT)").replace("group_training", "기술훈련 집단(정서조절, 의사소통 기술 등)")
        treatment_rank_trans = ("이와 유사한 사례를 상담심리 전문가 집단이 검토했을 때 제안한 <상담 시 접근방법> 추천순위는 다음과 같습니다: "
                                + str(treat_1) + " -> " + str(treat_2) + " -> " + str(treat_3) + " -> " + str(treat_4) + " -> " + str(treat_5) )
        print(treatment_rank_trans)
        print()
        target_1 = inter_target_rank.split("=")[0]
        target_2 = inter_target_rank.split("=")[1].split("; ")[1]
        target_3 = inter_target_rank.split("=")[2].split("; ")[1]
        target_4 = inter_target_rank.split("=")[3].split("; ")[1]
        target_5 = inter_target_rank.split("=")[4].split("; ")[1]


	#내림차순 정렬된 순서대로 해당 개입의 우선순위(주제 이름) 불러오기 
        target_1 = target_1.replace("trait", "내담자의 성격과 기질").replace("emotion", "내담자의 정서( 및 정서조절 문제)").replace("thoughts", "내담자의 사고와 신념").replace("past exp.", "내담자의 과거 경험(애착, 불안정한 아동기 등)").replace("present exp.", "내담자의 현재 삶(평소 생활, 중요한 관계 등)")
        target_2 = target_2.replace("trait", "내담자의 성격과 기질").replace("emotion", "내담자의 정서( 및 정서조절 문제)").replace("thoughts", "내담자의 사고와 신념").replace("past exp.", "내담자의 과거 경험(애착, 불안정한 아동기 등)").replace("present exp.", "내담자의 현재 삶(평소 생활, 중요한 관계 등)")
        target_3 = target_3.replace("trait", "내담자의 성격과 기질").replace("emotion", "내담자의 정서( 및 정서조절 문제)").replace("thoughts", "내담자의 사고와 신념").replace("past exp.", "내담자의 과거 경험(애착, 불안정한 아동기 등)").replace("present exp.", "내담자의 현재 삶(평소 생활, 중요한 관계 등)")
        target_4 = target_4.replace("trait", "내담자의 성격과 기질").replace("emotion", "내담자의 정서( 및 정서조절 문제)").replace("thoughts", "내담자의 사고와 신념").replace("past exp.", "내담자의 과거 경험(애착, 불안정한 아동기 등)").replace("present exp.", "내담자의 현재 삶(평소 생활, 중요한 관계 등)")
        target_5 = target_5.replace("trait", "내담자의 성격과 기질").replace("emotion", "내담자의 정서( 및 정서조절 문제)").replace("thoughts", "내담자의 사고와 신념").replace("past exp.", "내담자의 과거 경험(애착, 불안정한 아동기 등)").replace("present exp.", "내담자의 현재 삶(평소 생활, 중요한 관계 등)")
        inter_target_rank_trans = ("아울러, 전문가들은 이 사례에 대하여 <개입의 우선순위>를 다음와 같이 제안했습니다: "
                                   + str(target_1) + " -> " + str(target_2) + " -> " + str(target_3) + " -> " + str(target_4) + " -> " + str(target_5) )
    
    results5.write(str(num) + "\t" + token_case + "\t" + str(group) + "\t" +
                   group_trans + "\t" + flag_trans + "\t" + topic_profile_trans + "\t" +
                   treatment_rank_trans + "\t" + treat_1 + "\t" + treat_2 + "\t" + treat_3 + "\t" + treat_4 + "\t" + treat_5 + "\t" +
                   inter_target_rank_trans + "\t" + target_1 + "\t" + target_2 + "\t" + target_3 + "\t" + target_4 + "\t" + target_5 + "\n") #데이터 시각화 이전 모든 결과 저장 
    pie_dict = {topic_name_0: topic_est_0, #토픽 프로파일 파이 차트로 시각화 
                topic_name_1: topic_est_1,
                topic_name_2: topic_est_2,
                topic_name_3: topic_est_3,
                topic_name_4: topic_est_4,
                topic_name_5: topic_est_5,
                topic_name_6: topic_est_6,
                topic_name_7: topic_est_7,
                topic_name_8: topic_est_8,
                topic_name_9: topic_est_9 }
    pie_dict_clean = dic_out = {x:y for x,y in pie_dict.items() if y!=0}
    pie_keys = list(pie_dict_clean.keys()) #파이 차트 key = 토픽 명
    pie_keys = str(pie_keys).replace("[","").replace("]","") 
    pie_values = pie_dict_clean.values() #파이 차트 value = 토픽 점유율 
    pie_values = str(pie_values).replace("dict_values","").replace("([","").replace("])","")
    ratio = pie_values.split(", ")
    labels = pie_keys.split(", ")
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    colors = ['darkslategrey', 'darkcyan', 'lightseagreen', 'lightblue', 'lightcyan', 'lightgray', 'lightgray', 'lightgray', 'lightgray', 'lightgray']
    plt.pie(ratio, startangle=260, counterclock=False, wedgeprops=wedgeprops, colors=colors) #autopct='%.1f%%', 
    plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10) #, shadow=True) #frameon=True, 
    fig1 = plt.figure()
    plt.close(fig1)
    plt.savefig('C:/Users/SYK/Desktop/0406results/0324_visual_piechart_' + str(trans_case) + '.jpg', dpi=300, bbox_inches='tight')
    plt.close() 
    token_case = str(token_case).replace(" ", ", ")
    tokens_list = token_case.split(", ")
    counts = Counter(tokens_list)
    tags = counts.most_common(100) 

    w_font_path = 'C:/Users/SYK/Desktop/HANYGO240.ttf'
    wc = WordCloud(font_path=w_font_path, background_color="white", max_font_size=60, prefer_horizontal= 1.0) #width = 000, height = 000, stopwords=stopwords #font_path=['C:/Windows/Fonts/MALGUN.TTF'], #사례에서 도출된 어근들로 워드 클라우드 구성(어근 단어 사용 빈도가 높을수록 워드 클라우드에 큰 크기로 표시) 
    cloud = wc.generate_from_frequencies(dict(tags))
    plt.imshow(cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    fig2 = plt.figure(figsize=(10,8))
    plt.close(fig2)
    plt.savefig('C:/Users/SYK/Desktop/0406results/0324_visual_w.cloud_' + str(trans_case) + '.jpg', dpi=700, bbox_inches='tight') 
    plt.close() 

    class PDF(FPDF): #결과 보고서 출력 및 저장을 위해 빈 pdf 파일 생성 
        def footer(self): 
            self.set_y(-15)
            self.add_font('고딕', fname=r'C:/Users/SYK/Desktop/NanumGothic.ttf', uni=True)
            self.set_font('고딕', '', 8)
            self.set_text_color(128)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    pdf = PDF() 
    def create_letterhead(pdf, WIDTH):
        pdf.image("C:/Users/SYK/Desktop/report_header_crop2.jpg", 0, 0, WIDTH)
    def create_title(title, pdf):
        pdf.add_font('HYGTRE', fname=r'C:/Users/SYK/Desktop/HYGTRE.TTF', uni=True)
        pdf.add_font('고딕', fname=r'C:/Users/SYK/Desktop/NanumGothic.ttf', uni=True)
        pdf.set_font('HYGTRE', '', 25)  
        pdf.ln(20)
        pdf.write(5, title)
        pdf.ln(10)
        #자동으로 검사 날짜 입력 
        pdf.set_font('고딕', '', 14)
        pdf.set_text_color(r=128,g=128,b=128)
        today = time.strftime("%d/%m/%Y")
        pdf.write(4, f'{today}')
        pdf.ln(20)
    def write_to_pdf(pdf, words):
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.set_font('고딕', '', 12)
        pdf.write(5, words)
    def write_bold_to_pdf(pdf, words):
        pdf.add_font('HYGTRE', fname=r'C:/Users/SYK/Desktop/HYGTRE.TTF', uni=True)
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.set_font('HYGTRE', '', 12)
        pdf.write(5, words)
    TITLE = "내담자 리포트"
    WIDTH = 210
    HEIGHT = 297
    pdf.add_page()
    create_letterhead(pdf, WIDTH)
    create_title(TITLE, pdf)

    #결과 보고서에 ‘검사 결과의 사용범위’ 안내문 포함 
    write_to_pdf(pdf, "  본 결과지는 귀하가 등록하신 자해 행동을 하는 내담자의 글(text)을 자동화 검사도구를 이용해 검사한 결과 리포트입니다." )
    write_to_pdf(pdf, "다음의 결과들은 자해 경험이 있는 청(소)년의 글 약 300건과 그에 대한 (사)한국상담심리학회 1급 상담심리전문가들의 판단을 바탕으로 추정한 것입니다." + "\n")
    write_to_pdf(pdf, "  여러 차례의 수행 테스트를 통해서 검사도구를 최적화했지만, 추정치를 기초로 한 이 결과는 잠정적이기 때문에, 본 결과지를 내담자의 자해 발견 초기에 <참고용>으로 사용해주시기 바랍니다.")
    write_to_pdf(pdf, "기타 세밀한 치료적 판단과 내담자 이해를 위해서는 전문가에 의한 구체적인 심리평가와 면담이 필요합니다.")  
    pdf.ln(15)
    write_bold_to_pdf(pdf, "1. 내담자의 글(원본)") 
    pdf.ln(10)
    write_to_pdf(pdf, "  " + org_case) 
    pdf.ln(15)
    write_bold_to_pdf(pdf, "2. 사례에 대한 잠정적인 평가") #자료집단에 대한 해설 
    pdf.ln(10)
    write_to_pdf(pdf, "  " + group_trans + "\n") # + "\n" + "  " + flag_trans)
    write_to_pdf(pdf, "  " + flag_trans  + "\n")
    write_to_pdf(pdf, "  " + DEP_trans)
    write_to_pdf(pdf, "  " + ANX_trans)
    pdf.ln(15)
    write_bold_to_pdf(pdf, "3. 내담자의 키워드") #워드 클라우드 그림 삽입
    pdf.ln(10)
    pdf.image('C:/Users/SYK/Desktop/0406results/0324_visual_w.cloud_' + str(trans_case) + '.jpg', w=170) #, 5, 200, WIDTH/1.5) #5, 200, WIDTH/2-10)
    pdf.ln(15)
    write_bold_to_pdf(pdf, "4. 호소문제") #토픽 프로파일 파이 차트 그림 삽입 
    pdf.ln(10)
    write_to_pdf(pdf, "  " + topic_profile_trans)
    pdf.ln(10)
    pdf.image('C:/Users/SYK/Desktop/0406results/0324_visual_piechart_' + str(trans_case) + '.jpg', w=170) #, 5, 200, WIDTH/1.5) #5, 200, WIDTH/2-10)
    pdf.ln(5)
    pdf.set_font('고딕', '', 8)
    pdf.set_text_color(r=128,g=128,b=128)
    pdf.cell(180, 10, "※ 괄호 안에 '더 세부적인 문제'로 표시된 것은 해당 주제에 대하여 더 깊은 탐색이 필요함을 나타냅니다.", 0, 0, 'C')
    pdf.ln(15)
    write_bold_to_pdf(pdf, "5. 상담 시 접근방법 제안")
    pdf.ln(10)
    write_to_pdf(pdf, "  " + treatment_intro + "." + "\n")
    write_to_pdf(pdf, "    (1) " + treat1 + "\n")
    write_to_pdf(pdf, "    (2) " + treat2 + "\n")
    write_to_pdf(pdf, "    (3) " + treat3 + "\n")
    write_to_pdf(pdf, "    (4) " + treat4 + "\n")
    write_to_pdf(pdf, "    (5) " + treat5)
    pdf.ln(15)
    write_bold_to_pdf(pdf, "6. 개입의 우선순위(주제) 제안")
    pdf.ln(10)
    write_to_pdf(pdf, "  " + inter_intro + "." + "\n")
    write_to_pdf(pdf, "    (1) " + inter1 + "\n")
    write_to_pdf(pdf, "    (2) " + inter2 + "\n")
    write_to_pdf(pdf, "    (3) " + inter3 + "\n")
    write_to_pdf(pdf, "    (4) " + inter4 + "\n")
    write_to_pdf(pdf, "    (5) " + inter5)
    pdf.set_font('HYGTRE', '', 12)
    pdf.cell(180, 10, "- 감사합니다. -", 0, 0, 'C')
    pdf.ln(10)
    pdf.set_font('고딕', '', 12)
    pdf.cell(180, 6, "확률추론법으로 얻은 잠정적인 결과이므로 참고용으로 사용하시기 바랍니다.", 0, 5, 'C')
    #pdf.ln(8)
    pdf.cell(180, 6, "사용하신 검사도구 및 본 결과에 대한 불편 또는 문의 사항은:", 0, 5, 'C')
    pdf.cell(180, 6, "alexk1129@yonsei.ac.kr(김서영, 연세대학교 심리학과)로 보내주시기 바랍니다.", 0, 0, 'C', link="mailto:alexk1129@yonsei.ac.kr")
    pdf.ln(10) 
    pdf.output("C:/Users/SYK/Desktop/0406results/Client_" + str(trans_case) + "_report_0324.pdf", 'F') #완성된 결과 보고서를 PC에 자동으로 저장 

    if os.path.isfile('C:/Users/SYK/Desktop/NanumGothic.cw127.pkl'):
        os.remove('C:/Users/SYK/Desktop/NanumGothic.cw127.pkl')
        #return 'okay'
    if os.path.isfile('C:/Users/SYK/Desktop/NanumGothic.pkl'):
        os.remove('C:/Users/SYK/Desktop/NanumGothic.pkl')
    if os.path.isfile('C:/Users/SYK/Desktop/HYGTRE.cw127.pkl'):
        os.remove('C:/Users/SYK/Desktop/HYGTRE.cw127.pkl')
    if os.path.isfile('C:/Users/SYK/Desktop/HYGTRE.pkl'):
        os.remove('C:/Users/SYK/Desktop/HYGTRE.pkl')

    trans_case += 1 
    
computer_results.close()
results5.close()
error5.close() #모든 파일을 닫고 검사 종료  
