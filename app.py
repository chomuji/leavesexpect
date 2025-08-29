import streamlit as st

# 1cm² 당 기공 밀도
stomatal_density = {
    "단풍잎": 72111.6,
    "테이블야자": 23041.5,
    "깻잎": 29387.2,
    "고무나무": 42760.7,
    "몬스테라": 12694.6,
    "스투키": 8675.1
}

# 기공 1개당 하루 CO₂ 흡수량(µg)
co2_per_stomata_per_day = 0.05

# CO₂ 단위 변환 계수
unit_conversion_co2 = {"µg":1, "mg":1e-3, "g":1e-6, "kg":1e-9}

st.title("🌿 잎 기공 수 및 CO₂ 흡수량 계산기")

st.markdown(
    """
    식물 종류와 잎 크기를 입력하면 해당 잎의 기공 수와 하루 CO₂ 흡수량을 계산합니다.
    스투키는 특수 처리되어 4배로 계산됩니다.
    """
)

# 사용자 입력
plant = st.selectbox("식물 선택", list(stomatal_density.keys()), index=0)
width = st.number_input("잎 가로(cm)", min_value=0.1, value=1.0, format="%.2f")
height = st.number_input("잎 세로(cm)", min_value=0.1, value=1.0, format="%.2f")
co2_unit = st.selectbox("CO₂ 단위 선택", ["µg","mg","g","kg"], index=0)

# 계산
if st.button("계산하기"):
    density = stomatal_density[plant]
    total_stomata = width * height * density
    co2_absorbed = total_stomata * co2_per_stomata_per_day

    # 스투키 특수 처리
    if plant == "스투키":
        total_stomata *= 4
        co2_absorbed *= 4

    co2_absorbed_converted = co2_absorbed * unit_conversion_co2[co2_unit]

    st.write(f"🌿 **{plant}** 잎 {width} x {height} cm")
    st.write(f"- 기공 수: **{int(total_stomata):,}개**")
    st.write(f"- 하루 CO₂ 흡수량: **{co2_absorbed_converted:,.4f} {co2_unit}**")
