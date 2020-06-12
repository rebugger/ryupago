import os
import sys
import urllib.request
import json
import random

# Ryu's papago account..
api_config = {
	"id" : 'mJeiGZ2YNbi8ihzRjrNI',
	"secret" : 'ar0E8CVCux'	
}

# end
print('------------------------------------------------------------------------')
print()
inputText = urllib.parse.quote(input('[ryutakoo][input]: ')) #한글 인코딩 적용
print()
print('------------------------------------------------------------------------')
print()
#1. 어떤 언어로 번역할 건지 정한다.
def typeCheck() : 
	initType = ''
	 #첫번째 글자가 한글이면 영어로, 영어면 한글로 번역 시도
	initText = ''

	if len(inputText) == 0: 
		print('검색어가 없습니다. 재실행해주세염')
		sys.exit(1) # 입력 값이 없으므로 강제종료
	else : 
		initText = inputText[0]
		if initText == '%' : 		#print('한글입력되었습니다 영어로 번역합니다')
			initType = 1
		elif initText != '%' : 	
			initType = 2 # print('영어입니다. 한글로 번역합니다..')
		else :
			
			initType = randinit(1,2)

	return initType


#2. 번역 타입 지정
def typeSelect(tType) : 
	lang1 ='' #lang1 : 번역이 필요한 대상 
	lang2 ='' #lang2 : 번역될 대상

	if tType == 1 : #한글 -> 영어
		# print('한글 -> 영어')
		lang1 = 'ko'
		lang2 = 'en'
	elif tType == 2 : 	 #영어 -> 한글
		# print('영어 -> 한글')
		lang1 = 'en'
		lang2 = 'ko'
	else :
		print('알 수 없는 타입이니 종료처리')
		sys.exit(1)

	return lang1, lang2

#3. 파파고 OpenAPi 설정 후 전달한다.
def papagoAPI (rtnLanguage) : 
	url = "https://openapi.naver.com/v1/papago/n2mt"
	data = "source="+rtnLanguage[0]+"&target="+rtnLanguage[1]+"&text=" + inputText

	# 전송하기
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",api_config['id'])
	request.add_header("X-Naver-Client-Secret",api_config['secret'])
	# 응답
	response = urllib.request.urlopen(request, data=data.encode("utf-8"))
	rescode = response.getcode()

	if(rescode==200):
	    response_body = response.read().decode('utf-8')
	    response_json = json.loads(response_body) #JSON 형변환
	    response_result = str(response_json['message']['result']['translatedText']) #번역 값만 가져오기
	    print('[ryutakoo][Result]: ' + response_result)
	else:
	    print("Error Code:" + rescode)


def main() : 
	rtnType = typeCheck()
	rtnLang = typeSelect(rtnType)
	papagoAPI(rtnLang)
	print()
	print('------------------------------------------------------------------------')

main()

#검색어





