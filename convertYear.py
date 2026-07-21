import streamlit as st
st.title("เเอพพลิเคชั่นเเปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการดัดแปลง",value=2569)
ce_year=bh_year-543
st.header(f"xu พ.ส. คือ ; {ce_year}")
