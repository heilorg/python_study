# Write your code here :-)
alphabet = input("영어 소문자 하나를 입력해 주세요 : ");
result = "";
if alphabet == "a" or alphabet == "e" or alphabet == "o" or alphabet == "i" or alphabet == "u" :
    result = "모음"
else :
    result = "자음"
print("입력된 문자 " + alphabet + "는 " + result + "입니다.");
