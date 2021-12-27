import pandas as pd

# ポケモンが持つタイプを返すモジュール
import collePokeType as collePT


# 18タイプ
typeTupple = ("ノーマル", "ほのう", "みず", "くさ", "でんき", "こおり", "かくとう", "どく", "じめん",
              "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー")


# calcPokeType.pyのメインメソッド
def calPokeTypeMain(receivePokeName):

    # 最終的に返信する文字列のリスト
    sendStrLst = []
    sendStr = ""
    
    # 入力されたポケモンが持つタイプを取得
    weakTypeLst = collePT.getTypeLst(receivePokeName)

    # 検索したポケモンがいなかったらエラーを返す
    if weakTypeLst == False :
        return False
    
    # 取得したタイプからタイプ相性を求める
    totalWeakType = calcType(weakTypeLst)
    
    # 返信する文字列が格納されたリストを返す
    sendStrLst = getSendStr(sendStrLst,totalWeakType)

    sendStr = receivePokeName
    sendStr += ":"
    for str in weakTypeLst:
        sendStr += str
        sendStr += ","

    sendStr = sendStr[:-1]
    sendStr += '\n\n'

    # 返ってきたリストを分解する
    for str in sendStrLst:
        sendStr += str
        sendStr += '\n'

    sendStr = sendStr[:-1]

    return sendStr


# タイプ相性を求めるメソッド
def calcType(receiveLst):
    
    totalWeakType = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    # リストのタイプ数分ループ
    for type in receiveLst :
        #無
        if type == 'ノーマル' :
            totalWeakType[6] -= 1
            totalWeakType[13] = 10
        #炎
        elif type == 'ほのお' :
            totalWeakType[1] += 1
            totalWeakType[2] -= 1
            totalWeakType[3] += 1
            totalWeakType[5] += 1
            totalWeakType[8] -= 1
            totalWeakType[11] += 1
            totalWeakType[12] -= 1
            totalWeakType[16] += 1
            totalWeakType[17] += 1
        #水
        elif type == 'みず' :
            totalWeakType[1] += 1
            totalWeakType[2] += 1
            totalWeakType[3] -= 1
            totalWeakType[4] -= 1
            totalWeakType[5] += 1
            totalWeakType[16] += 1
        #草
        elif type == 'くさ' :
            totalWeakType[1] -= 1
            totalWeakType[2] += 1
            totalWeakType[3] += 1
            totalWeakType[4] += 1
            totalWeakType[5] -= 1
            totalWeakType[7] -= 1
            totalWeakType[8] += 1
            totalWeakType[9] -= 1
            totalWeakType[11] -= 1
        #電
        elif type == 'でんき' :
            totalWeakType[4] += 1
            totalWeakType[8] -= 1
            totalWeakType[9] += 1
            totalWeakType[16] += 1
        #氷
        elif type == 'こおり' :
            totalWeakType[1] -= 1
            totalWeakType[5] += 1
            totalWeakType[7] -= 1
            totalWeakType[12] -= 1
            totalWeakType[16] -= 1
        #闘
        elif type == 'かくとう' :
            totalWeakType[9] -= 1
            totalWeakType[10] -= 1
            totalWeakType[11] += 1
            totalWeakType[12] += 1
            totalWeakType[15] += 1
            totalWeakType[17] -= 1
        #毒
        elif type == 'どく' :
            totalWeakType[3] += 1
            totalWeakType[6] += 1
            totalWeakType[7] += 1
            totalWeakType[8] -= 1
            totalWeakType[10] -= 1
            totalWeakType[11] += 1
            totalWeakType[17] += 1
        #地
        elif type == 'じめん' :
            totalWeakType[2] -= 1
            totalWeakType[3] -= 1
            totalWeakType[4] = 10
            totalWeakType[5] -= 1
            totalWeakType[7] += 1
            totalWeakType[12] += 1
        #飛
        elif type == 'ひこう' :
            totalWeakType[3] += 1
            totalWeakType[4] -= 1
            totalWeakType[5] -= 1
            totalWeakType[6] += 1
            totalWeakType[8] = 10
            totalWeakType[11] += 1
            totalWeakType[12] -= 1
        #超
        elif type == 'エスパー' :
            totalWeakType[6] += 1
            totalWeakType[10] += 1
            totalWeakType[11] -= 1
            totalWeakType[13] -= 1
            totalWeakType[15] -= 1
        #虫
        elif type == 'むし' :
            totalWeakType[1] -= 1
            totalWeakType[3] += 1
            totalWeakType[6] += 1
            totalWeakType[8] += 1
            totalWeakType[9] -= 1
            totalWeakType[12] -= 1
            totalWeakType[17] += 1
        #岩
        elif type == 'いわ' :
            totalWeakType[0] += 1
            totalWeakType[1] += 1
            totalWeakType[2] -= 1
            totalWeakType[3] -= 1
            totalWeakType[6] -= 1
            totalWeakType[7] += 1
            totalWeakType[8] -= 1
            totalWeakType[9] += 1
            totalWeakType[16] -= 1
        #霊
        elif type == 'ゴースト' :
            totalWeakType[0] = 10
            totalWeakType[6] = 10
            totalWeakType[7] += 1
            totalWeakType[11] += 1
            totalWeakType[13] -= 1
            totalWeakType[15] -= 1
        #竜
        elif type == 'ドラゴン' :
            totalWeakType[1] += 1
            totalWeakType[2] += 1
            totalWeakType[3] += 1
            totalWeakType[4] += 1
            totalWeakType[5] -= 1
            totalWeakType[14] -= 1
            totalWeakType[17] -= 1
        #悪
        elif type == 'あく' :
            totalWeakType[6] -= 1
            totalWeakType[10] = 10
            totalWeakType[11] -= 1
            totalWeakType[13] += 1
            totalWeakType[15] += 1
            totalWeakType[17] -= 1
        #鋼
        elif type == 'はがね' :
            totalWeakType[0] += 1
            totalWeakType[1] -= 1
            totalWeakType[3] += 1
            totalWeakType[5] += 1
            totalWeakType[6] -= 1
            totalWeakType[7] = 10
            totalWeakType[8] -= 1
            totalWeakType[9] += 1
            totalWeakType[10] += 1
            totalWeakType[11] += 1
            totalWeakType[12] += 1
            totalWeakType[14] += 1
            totalWeakType[16] += 1
            totalWeakType[17] += 1
        #妖
        elif type == 'フェアリー' :
            totalWeakType[6] += 1
            totalWeakType[7] -= 1
            totalWeakType[11] += 1
            totalWeakType[14] = 10
            totalWeakType[15] += 1
            totalWeakType[16] -= 1
    return totalWeakType

def getSendStr(sendStrLst,totalWeakType):    
    for i in range(len(totalWeakType)):
        if (totalWeakType[i] >= 9) :
            sendStrLst.append(f'{typeTupple[i]} は 効果なしです')
        if (totalWeakType[i] == 2) :
            sendStrLst.append(f'{typeTupple[i]} は 1/4倍耐性です')
        if (totalWeakType[i] == 1) :
            sendStrLst.append(f'{typeTupple[i]} は 1/2倍耐性です')
        if (totalWeakType[i] == -1):
            sendStrLst.append(f'{typeTupple[i]} は 2倍弱点です')
        if (totalWeakType[i] == -2):
            sendStrLst.append(f'{typeTupple[i]} は 4倍弱点です')
    return sendStrLst
