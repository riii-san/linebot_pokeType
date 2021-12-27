import pandas as pd

# 入力されたポケモン名を返すメソッド
def getTypeLst(receivePokeName):
    
    # タイプが格納されりリスト
    pokeType =[]
    
    # カレントディレクトリに格納されているCSVを読みこむ
    df_PokeNameType = pd.read_csv("pokeNameType.csv",encoding="SHIFT-JIS")
    # NaN削除
    df_PokeNameType = df_PokeNameType.fillna("")
    
    try:
        # タイプをリストに格納
        pokeType.append(df_PokeNameType[df_PokeNameType['名前'] == receivePokeName]['タイプ1'].iloc[0])
        pokeType.append(df_PokeNameType[df_PokeNameType['名前'] == receivePokeName]['タイプ2'].iloc[0])
    except:
        return False
    
    # タイプ一つ持ちであればリストのタイプ2を削除
    if pokeType[1]=="" :
        pokeType.pop(-1)
    
    #タイプリストを返す
    return pokeType