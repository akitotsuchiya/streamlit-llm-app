from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import streamlit as st

from dotenv import load_dotenv
load_dotenv()

def get_llm_response(input_text, selected_expert):
    """
    LLMからの回答を取得する関数
    
    Args:
        input_text (str): ユーザーの入力テキスト
        selected_expert (str): 選択された専門家の種類
    
    Returns:
        str: LLMからの回答
    """
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    
    # 専門家の種類に応じてシステムメッセージを変更
    if selected_expert == "キャンプ":
        system_content = "あなたはキャンプの専門家です。キャンプに関する質問に対して、経験豊富なキャンプ愛好家として詳細で実用的なアドバイスを提供してください。"
    elif selected_expert == "ギター":
        system_content = "あなたはギターの専門家です。ギターに関する質問に対して、経験豊富なギタリストとして詳細で実用的なアドバイスを提供してください。"
    else:
        system_content = "You are a helpful assistant."
    
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_text),
    ]
    
    result = llm(messages)
    return result.content

# アプリのタイトルと説明
st.title("Lesson21:Streamlitを活用したLLMアプリ")

st.write("## アプリの概要")
st.write("このアプリでは、選択した専門分野のエキスパートとしてLLMに質問することができます。")
st.write("専門家を選択して、その分野に関する質問を入力してください。")

st.write("## 操作方法")
st.write("1. 下のラジオボタンから専門家を選択してください")
st.write("2. 入力フォームに質問を入力してください")
st.write("3. 「実行」ボタンをクリックして回答を取得してください")

st.divider()

# 専門家の選択
selected_item = st.radio(
    "専門家を選択してください。",
    ["キャンプ", "ギター"]
)

st.divider()

# 入力フォーム
if selected_item == "キャンプ":
    input_message = st.text_input(label="キャンプについての質問を入力してください。")
else:
    input_message = st.text_input(label="ギターについての質問を入力してください。")

# 実行ボタンと結果表示
if st.button("実行"):
    if input_message:
        st.divider()
        
        with st.spinner("回答を生成中..."):
            try:
                response = get_llm_response(input_message, selected_item)
                st.write("### 回答")
                st.write(response)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
                st.write("APIキーが正しく設定されているか確認してください。")
    else:
        st.warning("質問を入力してください。")