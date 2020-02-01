import pandas as pd
import random
import matplotlib.pyplot as plt
from apyori import apriori


store_data = pd.read_csv('store_data.csv', header=None)
store_data.head()

#Preprocessing
records = []
for i in range(0, len(store_data)):
    tempList = []
    for j in range(0,20):
        if str(store_data.values[i,j]) == 'nan':
            break
        tempList.append(str(store_data.values[i,j]))
    records.append(tempList)
#Dane wejściow
print()
print()
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)

for i in range(0,20):
    print("KOSZYK #"+str(i)+":"+str(records[i]))

#Wyświetlanie wyników
for item in association_results:

    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

support=rules.as_matrix(columns=['support'])
confidence=rules.as_matrix(columns=['confidence'])



#EFEKT:

#DANE WEJŚCIOWE:

KOSZYK #0:['shrimp', 'almonds', 'avocado', 'vegetables mix', 'green grapes', 'whole weat flour', 'yams', 'cottage cheese', 'energy drink', 'tomato juice', 'low fat yogurt', 'green tea', 'honey', 'salad', 'mineral water', 'salmon', 'antioxydant juice', 'frozen smoothie', 'spinach', 'olive oil']
KOSZYK #1:['burgers', 'meatballs', 'eggs']
KOSZYK #2:['chutney']
KOSZYK #3:['turkey', 'avocado']
KOSZYK #4:['mineral water', 'milk', 'energy bar', 'whole wheat rice', 'green tea']
KOSZYK #5:['low fat yogurt']
KOSZYK #6:['whole wheat pasta', 'french fries']
KOSZYK #7:['soup', 'light cream', 'shallot']
KOSZYK #8:['frozen vegetables', 'spaghetti', 'green tea']
KOSZYK #9:['french fries']
KOSZYK #10:['eggs', 'pet food']
KOSZYK #11:['cookies']
KOSZYK #12:['turkey', 'burgers', 'mineral water', 'eggs', 'cooking oil']
KOSZYK #13:['spaghetti', 'champagne', 'cookies']
KOSZYK #14:['mineral water', 'salmon']
KOSZYK #15:['mineral water']
KOSZYK #16:['shrimp', 'chocolate', 'chicken', 'honey', 'oil', 'cooking oil', 'low fat yogurt']
KOSZYK #17:['turkey', 'eggs']
KOSZYK #18:['turkey', 'fresh tuna', 'tomatoes', 'spaghetti', 'mineral water', 'black tea', 'salmon', 'eggs', 'chicken', 'extra dark chocolate']
KOSZYK #19:['meatballs', 'milk', 'honey', 'french fries', 'protein bar']

#WYPRODUKOWANE REGUŁY:

Rule: chicken -> light cream
Support: 0.004532728969470737
Confidence: 0.29059829059829057
Lift: 4.84395061728395
=====================================
Rule: escalope -> mushroom cream sauce
Support: 0.005732568990801226
Confidence: 0.3006993006993007
Lift: 3.790832696715049
=====================================
Rule: escalope -> pasta
Support: 0.005865884548726837
Confidence: 0.3728813559322034
Lift: 4.700811850163794
=====================================
Rule: herb & pepper -> ground beef
Support: 0.015997866951073192
Confidence: 0.3234501347708895
Lift: 3.2919938411349285
=====================================
Rule: tomato sauce -> ground beef
Support: 0.005332622317024397
Confidence: 0.3773584905660377
Lift: 3.840659481324083
=====================================
Rule: whole wheat pasta -> olive oil
Support: 0.007998933475536596
Confidence: 0.2714932126696833
Lift: 4.122410097642296
=====================================
Rule: pasta -> shrimp
Support: 0.005065991201173177
Confidence: 0.3220338983050847
Lift: 4.506672147735896
=====================================
Rule: shrimp -> chocolate
Support: 0.005332622317024397
Confidence: 0.23255813953488375
Lift: 3.2545123221103784
=====================================
Rule: spaghetti -> cooking oil
Support: 0.004799360085321957
Confidence: 0.5714285714285714
Lift: 3.2819951870487856
=====================================
Rule: spaghetti -> ground beef
Support: 0.008665511265164644
Confidence: 0.31100478468899523
Lift: 3.165328208890303
=====================================
Rule: olive oil -> milk
Support: 0.004799360085321957
Confidence: 0.20338983050847456
Lift: 3.088314005352364
=====================================
Rule: shrimp -> mineral water
Support: 0.007199040127982935
Confidence: 0.30508474576271183
Lift: 3.200616332819722
=====================================
Rule: spaghetti -> olive oil
Support: 0.005732568990801226
Confidence: 0.20574162679425836
Lift: 3.1240241752707125
=====================================
Rule: spaghetti -> shrimp
Support: 0.005999200106652446
Confidence: 0.21531100478468898
Lift: 3.0131489680782684
=====================================
Rule: spaghetti -> tomatoes
Support: 0.006665777896280496
Confidence: 0.23923444976076558
Lift: 3.4980460188216425
=====================================
Rule: spaghetti -> grated cheese
Support: 0.005332622317024397
Confidence: 0.3225806451612903
Lift: 3.283144395325426
=====================================
Rule: mineral water -> herb & pepper
Support: 0.006665777896280496
Confidence: 0.39062500000000006
Lift: 3.975682666214383
=====================================
Rule: spaghetti -> herb & pepper
Support: 0.006399146780429276
Confidence: 0.3934426229508197
Lift: 4.004359721511667
=====================================
Rule: olive oil -> milk
Support: 0.004932675643247567
Confidence: 0.22424242424242427
Lift: 3.40494417862839
=====================================
Rule: spaghetti -> shrimp
Support: 0.005999200106652446
Confidence: 0.5232558139534884
Lift: 3.005315360233627
=====================================
Rule: spaghetti -> olive oil
Support: 0.007199040127982935
Confidence: 0.20300751879699247
Lift: 3.0825089038385434
=====================================
Rule: soup -> olive oil
Support: 0.005199306759098787
Confidence: 0.22543352601156072
Lift: 3.4230301186492245
=====================================
Rule: pancakes -> olive oil
Support: 0.005065991201173177
Confidence: 0.20105820105820105
Lift: 3.0529100529100526
=====================================
Rule: spaghetti -> mineral water
Support: 0.004532728969470737
Confidence: 0.28813559322033894
Lift: 3.0228043143297376
=====================================

INTERPRETACJA:

Kupując spaghetti (ostatnie) istnieje 28% Szans że kupimy wodę mineralną



















