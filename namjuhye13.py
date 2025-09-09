import pandas as pd

df = pd.read_csv("gapminder.tsv", sep="\t")  # ← 실습용 tsv 파일 이름
print(df.head())

print(type(df))  #데이터프레임의 자료형 확인

print(df.shape)  #데이터의 행과 열의 크기에 대한 정보 확인 (행,열)

print(df.columns) #데이터의 열 정보 확인

print(df.dtypes)

print(df.info())

#판다스 -> 파이썬 : 자료형
#object -> string : 문자열
#int64 -> int : 정수
#float64 -> float : 소수점을 가진 숫자
#datetime64 -> datetime : 파이썬 표준 라이브러리인 datetime이 반환하는 자료형



#02-2 데이터 추출하기
#02-2-(1) 열 단위 데이터 추출하기
country_df=df['country']
print(type(country_df))

print(country_df.head())

print(country_df.tail())

df=df.drop([1704,1705,1706])
print(df)

print(country_df.tail())

df=pd.read_csv("gapminder.tsv",sep="\t")
df=df[:-3]
print(df)
print(df.tail())

subset=df[['country','continent','year']]  #df의 특정 열만 추출해서 subset에 저장
print(type(subset))
print(subset.head())
print(subset.tail())

#행 단위 데이터 추출하기 (loc / iloc)
#loc : 이름 기준
#iloc : 숫자 인덱스 (정수) 기준

#loc[0] : 레이블(이름)이 0인 행
#iloc[0] : 맨 첫 번째 행 (0번 위치)

#loc로 추출
print(df.loc[0])  #인덱스가 0인 행 데이터 추출
print(df.loc[121])

print(df.loc[1703]) #마지막 행 데이터 추출하는 방법 
print(df.tail(n=1)) #==


print(df.loc[[0,99,999]])  #여러 인덱스 한 번에 추출 


#iloc로 추출
print(df.iloc[0])
print(df.loc[0])

subset=df.loc[:,['year','pop']]
print(subset.head())

subset=df.iloc[:,[2,4,-1]]   #iloc 속성의 열 지정값에 문자열을 쓰면 안 됨 -> 모든 행에서 열 번호 2,4, 마지막 열만 가져온다라는 뜻


#range 메서드로 데이터 추출하기
#range 메서드 : 지정한 구간의 정수 리스트를 반환 (제네레이터 반환) / 
#iloc는 제네레이터로 데이터 추출 불가 

small_range=list(range(5))
print(small_range)

print(type(small_range))
subset=df.iloc[:,small_range]  #df.iloc의 데이터프레임에서 small_range 열만큼만 추출해서 subset에 저장
print(subset.head())

small_range=list(range(3,6))
print(small_range)

subset=df.iloc[:,small_range]
print(subset.head())


#range 메서드에 range(0,6,2)와 같이 3개의 인자를 전달하면 0부터 5까지 2만큼 건너뛰는 제네레이터를 생성함
small_range=list(range(0,6,2))
subset=df.iloc[:,small_range]
print(subset.head())   #country,year,pop 열만 추출 (0부터 5까지 2만큼 건너뛰기 때문에 0,2,4 열만 추출되려면)
      

#슬라이싱 구문과 range 메서드 비교하기 (실무에서는 슬라이싱을 더 많이 씀)
subset=df.iloc[:,:3]
print(subset.head())

subset=df.iloc[:,0:6:2]
print(subset.head())


#loc, iloc 속성 자유자재로 사용하기
print(df.iloc[[0,99,999],[0,3,5]])  #0,99,999번째 행의 0,3,5번째 열 데이터를 추출 -> 근데 이렇게 하면 나중에 어떤 데이터를 추출하기 위한 코드인지 파악하기 힘듬 -> loc 속성 (변수명)을 활용하여 열 지정값을 열 이름 지정
print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])  

print(df.loc[10:13,['country','lifeExp','gdpPercap']])




#02-3 기초적인 통계 계산하기
print(df.head(n=10)) #데이터 집합에서 0~9번째 데이터 추출하여 출력

#lifeExp 열을 연도별로 그룹화하여 평균 계산하기
# year 열로 그룹화 -> lifeExp 열의 평균 구하기 (groupby 메서드 활용)
# groupby : 데이터를 그룹화하고 그룹화된 데이터에 대한 연산을 수행하는 기능

print(df.groupby('year')['lifeExp'].mean())  #'year'기준으로 'lifeExp'를 평균  =  lifeExp 열을 연도별로 그룹화하여 평균

grouped_year_df=df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df)

grouped_year_df_lifeExp=grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))

mean_lifeExp_by_year=grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

multi_group_var=df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()   #인덱스는 (year, continent) 조합이고, 값은 lifeExp와 gdpPercap의 평균, () = 함수 실행,  [] = 컬럼 선택
print(multi_group_var)

#그룹화한 데이터 개수 세기 (빈도수) - nunique 메서드
print(df.groupby('continent')['country'].nunique())








#03 판다스 데이터프레임과 시리즈

#03-1 나만의 데이터 만들기 
import pandas as pd

#시리즈 만들기 -> 문자열을 인덱스로 지정 (Series 메서드의 index 인자를 사용) -> 데이터프레임 만들기
#03-1 (1) 시리즈 만들기
s=pd.Series(['banana',42])
print(s)


#03-1 (2) 문자열을 인덱스로 지정 / eg) person을 wes로, who를 creator로
s=pd.Series (['Wes McKinney','Creator of Pandas'])
print(s)

s=pd.Series(['Wes McKinney','Creator of Pandas'],index=['Person','Who'])
print(s)


#03-1 (3) 데이터프레임 만들기
scientists=pd.DataFrame({
    'Name':['Rosaline Franklin','William Gosset'],
    'Occupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1058-04-16','1937-10-16'],
    'Age':[37,61]})
print(scientists)


#03-1 (4) 만든 데이터 프레임에 인덱스 지정하기
scientists=pd.DataFrame(
    data={'Occupation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1058-04-16','1937-10-16'],
    'Age':[37,61]},
    index=['Rosaline Frankline','William Gosset'],
    columns=['Occupation','Born','Age','Died']
)
print(scientists)



#03-1 (5) 딕셔너리의 데이터 순서를 그대로 유지하면서 데이터프레임 만들기 

from collections import OrderedDict

scientists=pd.DataFrame(OrderedDict([
    ('Name',['Rosaline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1058-04-16','1937-10-16']),
    ('Age',[37,61])
])
)
print(scientists)




#03-2 시리즈 다루기 - 기초
#변수 (scientists)에 데이터프레임 준비 -> 


scientists=pd.DataFrame(
    data={'Occupation':['Chemist','Statistician'],
          'Born':['1920-07-20','1876-06-13'],
          'Died':['1958-04-16','1937-10-16'],
          'Age':[37,61]},
    index=['Rosaline Frankline','William Gosset'],
    columns=['Occupation','Born','Died','Age']
)



first_row=scientists.loc['William Gosset']
print(type(first_row))

print(first_row)


#시리즈 속성과 메서드 사용하기 - index, values, keys

#1. index 속성 사용하기 - 시리즈의 인덱스가 들어있음 
print(first_row.index) 

#2. values 속성 사용하기 - 시리즈의 데이터가 저장되어 있음 (데이터 내용)
print(first_row.values)

#3. keys 메서드 사용하기 - index 속성과 동일한 역할 / keys는 속성이 아닌 메서드 => 괄호를 써야함 [eg)메서드: print(first_row.keys()) / 속성: print(first_row.index)] 
print(first_row.keys())

#4.index 속성 응용하기
print(first_row[0])
print(first_row[1])

#5. keys 메서도 응용하기
print(first_row.keys()[0])


#시리즈의 기초 통계 메서드 사용하기
#(1) scientists의 age 열 추출
age=scientists['Age']
print(age)




#03-3 시리즈 다루기 - 응용 (불린 사용) -> 2장에서는 원하는 데이터를 추출할 때 특정 인덱스를 지정하여 추출함. 하지만 보통은 추출할 데이터의 정확한 인덱스를 모르기 때문에 특정 조건을 만족하는 값만 추출할 때 사용하는 불린을 이용함
scientists=pd.read_csv('../data/scientists.csv')
ages=scientists['Age']
print(ages.max())

print(ages.mean())

#불린 추출 - 평균보다 나이가 많은 사람의 데이터 추출

#과정1 
print(ages[ages>ages.mean()])

#과정2
print(ages>ages.mean())  #조건식을 만족한 값만 추출 (TRUE/FALSE)

#과정1 + 과정2  => 데이터에 대해 TRUE/FALSE 조건을 만들고 TRUE인 값만 뽑아내는 것 ==> 불린 추출
manual_bool_values=[True,True,False,False,True,True,False,True]
print(ages[manual_bool_values])

print(scientists)

#시리즈와 브로드캐스팅
print(ages+ages)
print(ages*ages)

#길이가 서로 다른 벡터를 연산할 때 (시리즈와 시리즈를 연산하는 경우 같은 인덱스끼리 연산 / 데이터 개수가 서로 다른 시리즈끼리 연산하면 일치하는 것까지만 계산, 나머지는 누락값 처리)
print(pd.Series([1,100]))
print(ages+pd.Series([1,100]))

#sort_index 메서드 사용
rev_ages=ages.sort_index(ascending=False) #인덱스 역순으로 데이터 정렬
print(rev_ages)


#아래 두 개 코드 결과값을 동일함. => 벡터와 벡터의 연산은 일치하는 인덱스의 값끼리 수행됨
print(ages*2)
print(rev_ages+ages)



#03-4 데이터프레임 다루기 - 데이터프레임도 불린 추출과 브로드캐스팅을 할 수 있음
#1. 불린 추출하기
print(scientists[scientists['Age']>scientists['Age'].mean()])
#2. 데이터프레임의 loc 속성에 길이가 4인 bool벡터 전달


#03-5 시리즈와 데이터프레임의 데이터 처리하기
#1. 열의 자료형 바꾸기와 새로운 열 추가하기
print(scientists['Born'].dtype)
print(scientists['Died'].dtype)

#2. born,died 열의 자료형 -> datetime 자료형으로 변경한 후 %Y-%m-%d로 지정
born_datetime=pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
print(born_datetime)

died_datetime=pd.to_datetime(scientists['Died'],format='%Y-%m-%d')
print(died_datetime)


#3. 데이터프레임에 각각의 값을 새로운 열로 추가  (scientists 데이터프레임에 born_datetime,died_datetime의 정보들이 새로운 두 개의 열로 추가된 거임)
scientists['born dt'],scientists['died_dt']=(born_datetime,died_datetime)
print(scientists.head())
print(scientists.shape)  #데이터프레임의 행,열 정보 확인


#4. 시간 계산 (died_dt-born_dt=얼마나 살았는지)
scientists['age_days_dt']=(scientists['died_dt']-scientists['born dt'])
print(scientists)


#5. 시리즈, 데이터프레임의 데이터 섞기
print(scientists['Age'])


#6.age 열의 데이터를 섞으려면 random 라이브러리를 불러와야함 (random 라이브러리에는 데이터를 섞어주는 shuffle 메서드가 있음)
import random
random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])


#7. 데이터프레임의 열 삭제하기
print(scientists.columns)


#8. drop 메서드를 이용하여 데이터프레임의 열(Age) 삭제하기
scientists_dropped=scientists.drop(['Age'],axis=1)    #첫번째 인자: 삭제할 열, 두 번째 인자: axis=1
print(scientists_dropped.columns)



#03-6 데이터 저장하고 불러오기 (피클, csv, tsv 파일로 저장하고 다시 불러오는 방법)

#1. 피클로 저장하기 - 데이터를 바이너리 형태로 직렬화한 오브젝트를 저장
names=scientists['Name']
names.to_pickle('../output/scientists_names_series.pickle')

scientists.to_pickle('../output/scientists_df.pickle')


scientist_names_from_pickle=pd.read_pickle('../output/scientists_names_series.pickle')
print(scientist_names_from_pickle)
scientists_from_pickle=pd.read_pickle('../output/scientists_df.pickle')
print(scientists_from_pickle)


#csv 파일과 tsv 파일로 저장하기 (csv: 데이터를 쉼표로 구분 / tsv: 데이터를 탭으로 구분)
names.to_csv('../output/scientists_names_series.csv')        #시리즈/데이터프레임을 csv파일로 저장
scientists.to_csv('../output/scientists_df.tsv',sep='\t')    #시리즈/데이터프레임을 tsv파일로 저장





#04 - 그래프 그리기

#04-1 데이터 시각화가 필요한 이유

#[앤스콤 데이터 집합 불러온 후 그래프 그리기]

#1.앤스콤 데이터 집합 불러오기
import seaborn as sns
anscombe=sns.load_dataset("anscombe")
print(anscombe)
print(type(anscombe))

# 2. matplotlib 라이브러리로 그래프 그리기
import matplotlib.pyplot as plt


#3. anscombe 데이터프레임의 dataset 열에서 데이터 값이 I인 것만 추출 (==첫 번째 데이터 그룹 추출)
dataset_1=anscombe[anscombe['dataset']=='I']  


#4. PLOT 메서드에 X.Y축  데이터를 전달하여 선 그래프 그리기 
plt.plot(dataset_1['x'],dataset_1['y'])
#.py 파일로 실행할 때에는 꼭 plt.show()해줘야 그래프 창이 뜸


#5. 점으로 그래프 그리기 (점그래프를 그리려면 o를 세 번째 인자로 전달하면 됨)
plt.plot(dataset_1['x'],dataset_1['y'],'o')



#앤스콤 데이터 집합 모두 사용하여 그래프 만들기

#matplotlib 라이브러리로 그래프 그리기
#1. 전체 그래프가 위치할 기본 틀 만들기
#2. 그래프를 그려 넣을 그래프 격자 만들기
#3. 격자에 그래프 하나씩 추가하기.(격자에 그래프가 추가되는 방향은 왼->오)
#4. 격자의 첫 번째 행이 다 차면 두 번째 행에 그래프를 그려넣음  (==앤스콤데이터 집합으로 그릴 그래프의 격자크기는 4- => 세 번째 그래프의 위치는 2행 1열)

#앤스콤데이터프레임의 dataset열의 값이   Ⅰ,Ⅱ,Ⅲ,Ⅳ인 것을 불린 추출하여 dataset_1,dataset_2,dataset_3,dataset_4에 저장
dataset_2=anscombe[anscombe['dataset']=='II']
dataset_3=anscombe[anscombe['dataset']=='III']
dataset_4=anscombe[anscombe['dataset']=='IV']


#1. 그래프 격자가 위치할 틀 만들기
fig=plt.figure()

#2. 그래프 격자 그리기 (add_subplot 메서드 사용 - 첫 번째 인자: 기본 틀의 행 크기, 두 번째 인자: 기본 틀의 열 크기)
axes1=fig.add_subplot(2,2,1)
axes2=fig.add_subplot(2,2,2)
axes3=fig.add_subplot(2,2,3)
axes4=fig.add_subplot(2,2,4)



#3. plot메서드에 데이터 전달하여 그래프 그리기 (그래프를 확인하려면 fig를 반드시 입력해야함)
axes1.plot(dataset_1['x'],dataset_1['y'],'o')
axes2.plot(dataset_2['x'],dataset_2['y'],'o')
axes3.plot(dataset_3['x'],dataset_3['y'],'o')
axes4.plot(dataset_4['x'],dataset_4['y'],'o')


#5. 그래프 격자에 제목 추가
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")




#6. 기본 틀에도 제목 추가 
fig.suptitle("Anscombe Data")
#그래프를 생성했을 때 각 그래프의 이름과 숫자가 겹쳐서 보임


#7. 이전 단계에서 발생한 문제를 해결하기 위해 tight_layout 메서드를 사용하여 레이아웃 조절
fig.tight_layout()



#04-2 matplotlib 라이브러리 자유자재로 사용하기
#기초 그래프 그리기

#1. tips 데이터 집합 불러온 후 변수 tips에 저장
tips=sns.load_dataset("tips")
print(tips.head())
print(type(tips))

fig=plt.figure()
axes1=fig.add_subplot(1,1,1)


#hist 메서드에 total_bill 열을 전달하여 히스토그램 만들기 (x축 간격: bins 인잣값으로 조정)
axes1.hist(tips['total_bill'],bins=10)
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')



#산점도 그래프 그리기 (산점도 그래프는 변수 2개 사용 -> 이변량 그래프)
#total_bill 열에 따른 tip 열의 분포를 나타낸 산점도 그래프 그리기
#-> 기본 틀과 그래프 격자 만들기 -> scatter 메서드에 total_bill, tips 열 전달

scatter_plot=plt.figure()
axes1=scatter_plot.add_subplot(1,1,1)
axes1.scatter(tips['total_bill'],tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')



#boxplot 메서드를 사용하여 박스 그래프 그리기 
#박스그래프 : 이산형 변수와 연속형 변수를 함께 사용하는 그래프 
# 이산형: female,male처럼 명확히 구분 가능, 연속형: tips처럼 명확하게 카운트 불가능)

boxplot=plt.figure()
axes1=boxplot.add_subplot(1,1,1)
axes1.boxplot([tips[tips['sex']=='Female']['tip'],
               tips[tips['sex']=='Male']['tip']],
               labels=['Female','Male'])

axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')



#다변량 그래프 그리기 
#다변량 그래프: 3개 이상의 변수를 사용한 그래프 - 

#1. 앞전에 실습한 산점도 그래프에 성별을 새로운 변수로 추가하기 
#- 성별은 색상으로 구분 / 근데 문자열(female, male)은 그래프에서 색상을 지정하는 값으로 사용할 수 없음
#==> 0,1과 같은 정수로 치환하는 함수를 만들어야함

def recode_sex(sex):
    if sex=='Female':
        return 0
    else:
        return 1

#record_sex 메서드가 반환한 값 (0,1)을 데이터프레임에 추가
tips['sex_color']=tips['sex'].apply(recode_sex)


#여기에 테이블당 인원 수도 추가 (인원 수: 점의 크기)
scatter_plot=plt.figure()
axes1=scatter_plot.add_subplot(1,1,1)
axes1.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size']*10,
    c=tips['sex_color'],
    alpha=0.5)
axes1.set_title('Total Bill vs Tip colored by Sex and Sized by Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')


#산점도 그래프와 히스토그램 한 번에 그려주는 jointplot 메서드 사용
joint=sns.jointplot(x='total_bill',y='tip',data=tips)
joint.set_axis_labels(xlabel='Total Bill',ylabel='Tip')
joint.fig.suptitle('Joint plot of total bill and tip',fontsize=10,y=1.03)


#산점도 그래프의 데이터를 구분하기 쉽게 그리고 싶다면 육각그래프 사용
#-> 산점도는 점이 겹쳐보여서 구분하기가 힘들기 때문에

hexbin=sns.jointplot(x="total_bill",y="tip",data=tips,kind="hex")
hexbin.set_axis_labels(xlabel='Total Bill',ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip',fontsize=10,y=1.03)


#이차원 밀집도 그리기 - kdeplot 메서드 (shade=True하면 음영 효과)




#바 그래프 그리기
ax=plt.subplots()
ax=sns.barplot(x='time',y='total_bill',data=tips)
ax.set_title('Bar plot of average total bill for time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')


#박스 그래프 그리기
ax=plt.subplots()
ax=sns.boxplot(x='time',y='total_bill',data=tips)
ax.set_title('Boxplot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')


#바이올린 그래프 그리기 
ax=plt.subplots()
ax=sns.violinplot(x='time',y='total_bill',data=tips)
ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')




#관계 그래프 그리기
fig=sns.pairplot(tips)


#04-4 데이터프레임과 시리즈로 그래프 그리기
ax=plt.subplots()
ax=tips['total_bill'].plot.hist()


#05 데이터 연결하기
#05-1 분석하기 좋은 데이터 
#1. 데이터 분석 목적에 맞는 데이터를 모아 새로운 표를 만들어야함
#2. 측정한 값은 행을 구성해야함
#3. 변수는 열로 구성해야함


#05-2 데이터 연결 기초
#데이터 연결하기
#1. concat 메서드로 데이터 연결하기

import pandas as pd
df1=pd.read_csv('../data/concat_1.csv')
df2=pd.read_csv('../data/concat_2.csv')
df3=pd.read_csv('../data/concat_3.csv')


#2. concat 메서드에 연결하려는 데이터프레임을 리스트에 담아 전달 -> 연결한 데이터프레임을 반환
#concat 메서드는 위->아래 방향으로 연결함

row_concat=pd.concat([df1,df2,df3])
print(row_concat)

#3. 행 데이터 추출
print(row_concat.iloc[3,]) #네 번째 행 추출

#4. 데이터프레임에 시리즈를 연결하기 위해 리스트를 시리즈로 변환
new_row_series=pd.Series(['n1','n2','n3','n4'])

#5. concat 메서드로 데이터프레임과 시리즈 연결
print(pd.concat([df1,new_row_series]))




#행 1개로 구성된 데이터프레임 생성하여 연결하기
new_row_df=pd.DataFrame([['n1','n2','n3','n4']],columns=['A','B','C','D'])
print(new_row_df)

print(pd.concat([df1,new_row_df]))



#다양한 방법으로 데이터 연결하기 
#1. ignore_index 인자 사용하기
row_concat_i=pd.concat([df1,df2,df3],ignore_index=True)
print(row_concat_i)


#2. 열 방향으로 데이터 연결하기 (axis 인자를 1로 설정)
col_concat=pd.concat([df1,df2,df3],axis=1)
print(col_concat)


#3. 같은 열 이름이 있는 데이터프레임에서 열 이름으로 데이터를 추출하면 해당 열 이름의 데이터를 모두 추출함
print(col_concat['A'])


#4. 간편하게 새로운 열 추가하기
col_concat['new_col_list']=['n1','n2','n3','n4']
print(col_concat)


#5. ignore_index=True 설정하여 열 이름 다시 지정
print(pd.concat([df1,df2,df3],axis=1,ignore_index=True))


#6. 공통 열과 공통 인덱스만 연결하기
df1.columns=['A','B','C','D']
df2.columns=['E','F','G','H']
df3.columns=['A','C','F','H']
print(df1)
print(type(df1))

print(df2)
print(type(df2))

print(df3)
print(type(df3))


#새롭게 열 이름을 부여한 데이터프레임 3개를 concat 메서드로 연결
row_concat=pd.concat([df1,df2,df3])
print(row_concat)   #생성된 데이터프레임에 누락값이 너무 많이 뜸

#공통 열만 골라서 연결하면 누락값 생기지 않음. (join 인자를 inner로 지정)
# 근데 공통 열이 없음
print(pd.concat([df1,df2,df3],join='inner'))   #df1,df2,df3의 교집합인 것을 추출


#df1, df3의 공통열 골라서 연결
print(pd.concat([df1,df3],ignore_index=False,join='inner'))

#데이터를 행 방향으로 연결
df1.index=[0,1,2,3]
df2.index=[4,5,6,7]
df3.index=[0,2,5,7]

print(df1)
print(df2)
print(df3)

col_concat=pd.concat([df1,df2,df3],axis=1)
print(col_concat)

#df1, df3의 공통 행만 골라서 연결
print(pd.concat([df1,df3],axis=1,join='inner'))




#05-3 데이터 연결 마무리
#merge 메서드 사용 
person=pd.read_csv('../data/survey_person.csv')
site=pd.read_csv('../data/survey_site.csv')
survey=pd.read_csv('../data/survey_survey.csv')
visited=pd.read_csv('../data/survey_visited.csv')

print(person)
print(site)
print(survey)
print(visited)

visited_subset=visited.loc[[0,2,6],]

#merge 메서드: 왼쪽 데이터프레임의 열과 오른쪽 데이터프레임의 열 값이 일치하면 왼쪽을 기준으로 연결함
o2o_merge=site.merge(visited_subset,left_on='name',right_on='site')
print(o2o_merge)


#site,visited 데이터프레임을 이용하여 데이터 연결
m2o_merge=site.merge(visited,left_on='name',right_on='site')
print(m2o_merge)


#(person,survey),(visited,survey)를 각각 merge 메서드로 연결
ps=person.merge(survey,left_on='ident',right_on='person')
vs=visited.merge(survey,left_on='ident',right_on='taken')

print(ps)
print(vs)

ps_vs=ps.merge(vs,left_on=['ident','taken','quant','reading'],right_on=['person','ident','quant','reading'])


#06 누락값 처리하기
#06-1 누락값 확인하기


import pandas as pd
import numpy as np

print(pd.isnull(np.nan))   # True
print(pd.notnull(42))


#누락값이 생기는 이유
#1. 누락값이 포함된 데이터 집합을 연결했을 때
visited=pd.read_csv('../data/survey_visited.csv')
survey=pd.read_csv('../data/survey_survey.csv')

print(visited)
print(survey)

vs=visited.merge(survey,left_on='ident',right_on='taken')
print(vs)



#2. 데이터를 입력할 때 누락값이 생기는 경우
#3. 범위를 지정하여 데이터를 추출할 때 누락값이 생기는 경우
gapminder=pd.read_csv('../data/gapminder.tsv',sep='\t')

life_exp=gapminder.groupby(['year'])['lifeExp'].mean()  #gapminder 데이터프레임을 연도별로 그룹화한 후 lifeExp의 평균을 구한 것
print(life_exp)



#누락값의 개수 구하기
ebola=pd.read_csv('../data/country_timeseries.csv')

#count 메서드로 누락값이 아닌 값의 개수 구하기
print(ebola.count())

#shape[0]에 전체 행의 데이터 개수가 저장되어 있음을 이용하면 shape[0]에서 누락값이 아닌 값의 개수를 빼면 누락값의 개수를 구할 수 있음
num_rows=ebola.shape[0]
num_missing=num_rows-ebola.count() #누락값의 개수
print(num_missing)


#시리즈에 포함된 value_counts 메서드는 지정한 열의 빈도를 구하는 메서드
print(ebola.Cases_Guinea.value_counts(dropna=False).head()) #value_counts 메서드를 사용하여 Cases_Guinea열의 누락값 개수 구하기


#누락값 처리하기
#1. 누락값 삭제하기
print(ebola.shape) #데이터 구조 확인
ebola_dropna=ebola.dropna()  #결측값을 제거한 상태
print(ebola_dropna.shape)    #결측값을 제거한 상태에서 구조 확인
print(ebola_dropna)


#누락값이 포함된 데이터 계산하기
ebola['Cases_multiple']=ebola['Cases_Guinea']+ebola['Cases_Liberia']+ebola['Cases_SierraLeone'] 
#--> 누락값이 존재하는 열들을 가지고 ebola 발병 수의 합을 계산
#==> 누락값이 하나라도 존재하는 행은 계산 결과가 nan이 되었음

ebola_subset=ebola.loc[:,['Cases_Guinea','Cases_Liberia','Cases_SierraLeone','Cases_multiple']]
print(ebola_subset.head(n=10))


print(ebola.Cases_Guinea.sum(skipna=True))
print(ebola.Cases_Guinea.sum(skipna=False))


#7 - 
import pandas as pd
pew = pd.read_csv('../data/pew.csv')
print(pew.head())


print(pew.iloc[:, 0:6])


pew_long = pd.melt(pew, id_vars='religion')
print(pew_long.head())


pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
print(pew_long.head())


billboard = pd.read_csv('../data/billboard.csv')

print(billboard.iloc[0:5, 0:16])


billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='week', value_name='rating')

print(billboard_long.head())



ebola = pd.read_csv('../data/country_timeseries.csv')
print(ebola.columns)


print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])


ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
print(ebola_long.head())


variable_split = ebola_long.variable.str.split('_')

print(variable_split[:5])


print(type(variable_split))


print(type(variable_split[0]))


status_values = variable_split.str.get(0) 
country_values = variable_split.str.get(1)

print(status_values[:5])


print(status_values[-5:])


print(country_values[:5])


print(country_values[-5:])

ebola_long['status'] = status_values 
ebola_long['country'] = country_values
print(ebola_long.head())


#8
#자료형을 자유자재로 변환하기 ─ astype 메서드
import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(str) 
print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(float) 
print(tips.dtypes)


# 잘못 입력한 문자열 처리하기 ─ to_numeric 메서드
tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'

print(tips_sub_miss)
print(tips_sub_miss.dtypes)


tips_sub_miss['total_bill'] = pd.to_numeric( tips_sub_miss['total_bill'], errors='ignore')

print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric( tips_sub_miss['total_bill'], errors='coerce')

print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric( tips_sub_miss['total_bill'], errors='coerce', downcast='float')

print(tips_sub_miss.dtypes)



# 문자열을 카테고리로 변환하기
tips['sex'] = tips['sex'].astype('str') 
print(tips.info())

tips['sex'] = tips['sex'].astype('category') 
print(tips.info())




#9
word = 'grail'
sent = 'a scratch'
print(word[0])

print(sent[0])
print(word[0:3])

print(sent[-1])
print(sent[-9:-8])
print(sent[0:-8])


d1 = '40°' 
m1 = "46'" 
s1 = '52.837"' 
u1 = 'N'

d2 = '73°' 
m2 = "58'" 
s2 = '26.302"' 
u2 = 'W'

coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
print(coords)


#splitlines 메서드
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together. 
""" 
print(multi_str)

multi_str_split = multi_str.splitlines() 
print(multi_str_split)

guard = multi_str_split[::2] 
print(guard)


#replace 메서드
guard = multi_str.replace("Guard: ", "").splitlines()[::2] 
print(guard)



#문자열 포매팅 하기
var = 'flesh wound' 
s = "It's just a {}!"

print(s.format(var))

print(s.format('scratch'))

s = """Black Knight: 'Tis but a {0}.
King Arthur: A {0}? Your arm's off!
""" 
print(s.format('scratch'))


s = 'Hayden Planetarium Coordinates: {lat}, {lon}' 
print(s.format(lat='40.7815° N', lon='73.9733° W'))



#숫자 데이터 포매팅하기
print('Some digits of pi: {}'.format(3.14159265359))
print("In 2005, Lu Chao of China recited {:,} digits of pi".format(67890))
print("I remember {0:.4} or {0:.4%} of what Lu Chao recited".format(7/67890))
print("My ID number is {0:05d}".format(42))



#%로 포매팅하기
s = 'I only know %d digits of pi' % 7 
print(s)

print('Some digits of %(cont)s: %(value).2f' % {'cont': 'e', 'value': 2.718})


#f-strings으로 포매팅하기
var = 'flesh wound' 
s = f"It's just a {var}!" 
print(s)

lat='40.7815°N' 
lon='73.9733°W' 
s = f'Hayden Planetarium Coordinates: {lat}, {lon}' 
print(s)

#compile 메서드로 정규식 메서드 사용하기 
p = re.compile('\d{10}') 
s = '1234567890' 
m = p.match(s) 
print(m)




#10

#제곱함수와 n 제곱 함수 만들기
def my_sq(x):
    return x ** 2

def my_exp(x, n):
    return x ** n

print(my_sq(4))

print(my_exp(2, 4))



# 시리즈와 데이터프레임에 apply 메서드 사용하기
import pandas as pd

df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]}) 

print(df)

print(df['a'] ** 2)

sq = df['a'].apply(my_sq) 
print(sq)


ex = df['a'].apply(my_exp, n=2) 
print(ex)


ex = df['a'].apply(my_exp, n=3) 
print(ex)

#데이터프레임과 apply 메서드 사용하기
df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]}) 
print(df)

def print_me(x): 
    print(x)

print(df.apply(print_me, axis=0))

print(df['a'])

print(df['b'])

def avg_3(x, y, z):
    return (x + y + z) / 3

print(df.apply(avg_3))


def avg_3_apply(col):
    x = col[0] 
    y = col[1] 
    z = col[2] 
    return (x + y + z) / 3


print(df.apply(avg_3_apply))

def avg_3_apply(col):
    sum = 0
    for item in col:
         sum += item
    return sum / df.shape[0]

def avg_2_apply(row):
    sum = 0
    for item in row:
        sum += item
    return sum / df.shape[1]

print(df.apply(avg_2_apply, axis = 1))

# 데이터프레임의 누락값을 처리한 다음 apply 메서드 사용하기
import seaborn as sns

titanic = sns.load_dataset("titanic")

print(titanic.info())

import numpy as np

def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count

cmis_col = titanic.apply(count_missing)
print(cmis_col)

def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem

pmis_col = titanic.apply(prop_missing)
print(pmis_col)


def prop_complete(vec):
    return 1 - prop_missing(vec)


# 데이터프레임의 누락값을 처리하기 ― 행 방향
cmis_row = titanic.apply(count_missing, axis=1)
pmis_row = titanic.apply(prop_missing, axis=1)
pcom_row = titanic.apply(prop_complete, axis=1)

print(cmis_row.head())

print(pmis_row.head())

print(pcom_row.head())

titanic['num_missing'] = titanic.apply(count_missing, axis=1)

print(titanic.head())
print(titanic.loc[titanic.num_missing > 1, :].sample(10))

#11
# groupby 메서드로 평균값 구하기
import pandas as pd 
df = pd.read_csv('../data/gapminder.tsv', sep='\t')

avg_life_exp_by_year = df.groupby('year').lifeExp.mean() 
print(avg_life_exp_by_year)

# avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean()
# print(avg_life_exp_by_year)

# 분할-반영-결합 과정 살펴보기
years = df.year.unique() 
print(years)

y1952 = df.loc[df.year == 1952, :] 
print(y1952.head())

y1952_mean = y1952.lifeExp.mean() 
print(y1952_mean)

y1957 = df.loc[df.year == 1957, :] 
y1957_mean = y1957.lifeExp.mean( )
print(y1957_mean)

y1962 = df.loc[df.year == 1962, :] 
y1962_mean = y1962.lifeExp.mean( )
print(y1962_mean)

y2007 = df.loc[df.year == 2007, :] 
y2007_mean = y2007.lifeExp.mean( )
print(y2007_mean)

df2 = pd.DataFrame({"year":[1952, 1957, 1962, 2007], 
                    "":[y1952_mean, y1957_mean,y1962_mean,y2007_mean]}) 
print(df2)


# 평균값을 구하는 사용자 함수와 groupby 메서드
def my_mean(values):
    n = len(values)
    
    sum = 0 
    for value in values:
        sum += value
    
    return sum / n

agg_my_mean = df.groupby('year').lifeExp.agg(my_mean) 
print(agg_my_mean)


# 두 개의 인잣값을 받아 처리하는 사용자 함수와 groupby 메서드
def my_mean_diff(values, diff_value):
    n = len(values) 
    sum = 0 
    for value in values:
        sum += value 
    mean = sum / n 
    return mean - diff_value

global_mean = df.lifeExp.mean() 
print(global_mean)

agg_mean_diff = df.groupby('year').lifeExp.agg(my_mean_diff, diff_value=global_mean) 
print(agg_mean_diff)



# 집계 메서드를 리스트, 딕셔너리에 담아 전달하기
import numpy as np
gdf = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std]) 
print(gdf)

gdf_dict = df.groupby('year').agg({'lifeExp': 'mean', 'pop': 'median', 'gdpPercap': 'median'}) 
print(gdf_dict)



# 누락값을 평균값으로 처리하기
import seaborn as sns 
import numpy as np

np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.NaN

print(tips_10)


count_sex = tips_10.groupby('sex').count() 
print(count_sex)

def fill_na_mean(x):
    avg = x.mean() 
    return x.fillna(avg)

total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
tips_10['fill_total_bill'] = total_bill_group_mean
print(tips_10)


# 데이터 필터링 - filter 메서드 사용하기
total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
tips_10['fill_total_bill'] = total_bill_group_mean
print(tips_10)

tips = sns.load_dataset('tips')

print(tips.shape)

print(tips['size'].value_counts())


tips_filtered = tips.\
    groupby('size').\
    filter(lambda x: x['size'].count() >= 30)

print(tips_filtered.shape)

print(tips_filtered['size'].value_counts())


# 그룹 오브젝트 저장하여 살펴보기
tips_10 = sns.load_dataset('tips').sample(10, random_state=42) 
print(tips_10)

grouped = tips_10.groupby('sex')
print(grouped)

print(grouped.groups)



# datetime 오브젝트 사용하기
from datetime import datetime
now1 = datetime.now() 
print(now1)

now2 = datetime.today()
print(now2) 

t1 = datetime.now() 
t2 = datetime(1970, 1, 1)
t3 = datetime(1970, 12, 12, 13, 24, 34)

print(t1)
print(t2)
print(t3)


diff1 = t1 - t2

print(diff1)
print(type(diff1))

diff2 = t2 - t1

print(diff2)
print(type(diff2))


# 문자열을 datetime 오브젝트로 변환하기
import pandas as pd 
import os
ebola = pd.read_csv('../data/country_timeseries.csv')


print(ebola.info())

ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola.info())

test_df1 = pd.DataFrame({'order_day':['01/01/15', '02/01/15', '03/01/15']})

test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
test_df1['date_dt2'] = pd.to_datetime(test_df1['order_day'], format='%m/%d/%y')
test_df1['date_dt3'] = pd.to_datetime(test_df1['order_day'], format='%y/%m/%d')

print(test_df1)

test_df2 = pd.DataFrame({'order_day':['01-01-15', '02-01-15', '03-01-15']})
test_df2['date_dt'] = pd.to_datetime(test_df2['order_day'], format='%d-%m-%y')

print(test_df2)


# 시계열 데이터를 구분해서 추출
now = datetime.now()
print(now)

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)

nowTime = now.strftime('%H:%M:%S')
print(nowTime) 

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime) 

# datetime 오브젝트로 변환하려는 열을 지정하여 데이터 집합 불러오기
ebola1 = pd.read_csv('../data/country_timeseries.csv', parse_dates=['Date']) 
print(ebola1.info())

# datetime 오브젝트에서 날짜 정보 추출하기
date_series = pd.Series(['2018-05-16', '2018-05-17', '2018-05-18'])
d1 = pd.to_datetime(date_series) 
print(d1)

print(d1[0].year)
print(d1[0].month)
print(d1[0].day)

# dt 접근자로 시계열 데이터 정리하기
ebola = pd.read_csv('../data/country_timeseries.csv')
ebola['date_dt'] = pd.to_datetime(ebola['Date'])


print(ebola[['Date', 'date_dt']].head())
print(ebola['date_dt'][3].year)
print(ebola['date_dt'][3].month)
print(ebola['date_dt'][3].day)

ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']].head())

ebola['month'], ebola['day'] = (ebola['date_dt'].dt.month, ebola['date_dt'].dt.day)

print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())

print(ebola.info())


#파산한 은행 개수 계산하기
banks = pd.read_csv('../data/banklist.csv') 
print(banks.head())

banks_no_dates = pd.read_csv('../data/banklist.csv')
print(banks_no_dates.info())

banks = pd.read_csv('../data/banklist.csv', parse_dates=[5, 6]) 
print(banks.info())

banks['closing_quarter'], banks['closing_year'] = (banks['Closing Date'].dt.quarter, banks['Closing Date'].dt.year)

print(banks.head())

closing_year = banks.groupby(['closing_year']).size()

print(closing_year)

closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()

print(closing_year_q)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax = closing_year.plot() 
plt.show()

fig, ax = plt.subplots() 
ax = closing_year_q.plot() 
plt.show()

# 시간 범위 생성하여 인덱스로 지정하기
ebola = pd.read_csv('../data/country_timeseries.csv', parse_dates=[0]) 
print(ebola.iloc[:5, :5])
print(ebola.iloc[-5:, :5])

head_range = pd.date_range(start='2014-12-31', end='2015-01-05') 
print(head_range)

ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
ebola_5.reindex(head_range)

print(ebola_5.iloc[:5, :5])





