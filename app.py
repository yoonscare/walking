import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="걷기와 노화 예방 대시보드",
    page_icon="👣",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 데이터 준비
# 건강수명 데이터
life_expectancy_data = pd.DataFrame({
    "국가": ["한국", "일본", "스웨덴", "영국", "미국"],
    "건강수명": [65.8, 74.1, 72.0, 71.4, 68.5],
    "기대수명": [82.7, 84.2, 82.4, 81.2, 78.9]
})

# 걷기 효과 데이터
walking_benefits_data = pd.DataFrame({
    "질환": ["심혈관질환", "치매", "당뇨병", "우울증", "뇌졸중"],
    "위험감소율(%)": [30, 25, 20, 15, 10]
})

# 연령대별 권장 걷기 시간 데이터
age_walking_time_data = pd.DataFrame({
    "연령대": ["30대", "40대", "50대", "60대", "70대 이상"],
    "권장시간(분)": [30, 35, 40, 45, 30]
})

# 시간대별 걷기 효과 데이터
time_effect_data = pd.DataFrame({
    "시간대": ["아침(6-8시)", "오전(9-11시)", "점심(12-14시)", "오후(16-18시)", "저녁(19-21시)"],
    "혈당조절효과": [60, 65, 70, 85, 75],
    "심혈관건강효과": [70, 75, 65, 90, 80]
})

# 걷기 방법 데이터
walking_methods = pd.DataFrame({
    "방법": ["싱글벙글 걷기", "파워 워킹", "노르딕 워킹"],
    "설명": [
        "대화가 가능한 강도로 걷는 방법으로, 스트레스 감소와 일상 건강 유지에 효과적입니다.",
        "최대심박수의 60~75%로 걷는 방법으로, 심폐지구력과 근력 강화에 효과적입니다.",
        "스틱을 활용하여 상체까지 함께 운동하는 방법으로, 전신 근력 강화와 칼로리 소모에 효과적입니다."
    ],
    "실천방법": [
        "자연스러운 속도로 걸으며 대화가 가능할 정도의 강도를 유지합니다. 천천히 시작해서 30분 이상 지속하는 것이 좋습니다.",
        "팔을 적극적으로 흔들며 보폭을 넓게 하고 속도를 높여 걷습니다. 심박수가 최대심박수의 60~75% 수준을 유지하도록 합니다.",
        "전용 스틱을 사용하여 스키 동작과 유사하게 팔과 다리를 함께 움직입니다. 스틱을 뒤로 밀며 상체 근육을 적극적으로 사용합니다."
    ],
    "심폐지구력": [60, 85, 80],
    "근력강화": [40, 70, 90],
    "스트레스감소": [90, 60, 65],
    "혈당조절": [50, 75, 80]
})

# 생활 지침 데이터
lifestyle_guidelines = pd.DataFrame({
    "시간대": ["아침 루틴", "식사 관리", "오후 활동", "저녁 루틴"],
    "내용": [
        "아침에 일어나서 10분 스트레칭 후 20분 걷기를 실천하세요. 혈액순환과 신진대사를 촉진합니다.",
        "식사 후 1시간이 지난 후 10-15분 가벼운 산책을 하면 혈당 조절에 효과적입니다.",
        "오후 4-6시에 30분 이상 걷기 운동을 하면 혈당 조절과 심혈관 건강에 가장 효과적입니다.",
        "저녁 식사 후 TV 시청 대신 15-20분 동네 한 바퀴 산책하고, 잠들기 1시간 전 가벼운 스트레칭으로 마무리하세요."
    ]
})

# 영양소 데이터
nutrition_data = pd.DataFrame({
    "영양소": ["필발", "시나몬", "사차인치", "콜라겐펩타이드"],
    "효과": [
        "항산화 작용, 혈관 기능 개선",
        "항염증 작용, 혈당 조절",
        "오메가-3 지방산, 항염증 작용",
        "관절 건강, 근육 회복"
    ]
})

# 사이드바
st.sidebar.title("걷기와 노화 예방")
st.sidebar.image(
    "https://images.unsplash.com/photo-1538370965046-79c0d6907d47?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    use_column_width=True
)

# 네비게이션
page = st.sidebar.radio(
    "페이지 선택",
    ["개요", "걷기 효과", "걷기 방법", "생활 지침"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**안내**: 이 대시보드는 걷기가 노화에 미치는 영향과 건강한 생활을 위한 데이터를 시각화하여 제공합니다.

**출처**: 이가세 미치야 지음, "걷기가 노화 속도를 결정한다", 빚은책들
""")

# 컬러 팔레트
colors = {
    "primary": "#1E88E5",
    "secondary": "#FBC02D",
    "success": "#4CAF50",
    "danger": "#F44336",
    "purple": "#9C27B0",
    "teal": "#009688"
}

# 개요 페이지
if page == "개요":
    st.title("걷기와 노화 예방 대시보드")
    
    st.markdown("""
    <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;color:#000;'>
    걷기는 단순한 신체활동이 아닌 노화를 늦추고 건강수명을 연장하는 가장 쉽고 효과적인 방법입니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 주요 인사이트와 차트를 두 컬럼으로 나누기
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("주요 인사이트")
        
        insights = [
            {"text": "한국의 건강수명은 <strong>65.8년</strong>으로 기대수명보다 <strong>16.9년</strong> 짧음", "color": "#E3F2FD"},
            {"text": "하체에 <strong>전체 근육의 70%</strong>가 집중되어 있음", "color": "#E8F5E9"},
            {"text": "걷기를 통해 생성되는 <strong>마이오카인</strong>이 치매와 알츠하이머 위험 감소", "color": "#F3E5F5"},
            {"text": "걷기는 모세혈관 소실현상을 막아 <strong>혈류 개선</strong>", "color": "#FFF8E1"},
            {"text": "걷기 최적 시간대는 <strong>오후 16~18시</strong>", "color": "#FFEBEE"}
        ]
        
        for insight in insights:
            st.markdown(f"""
            <div style='background-color:{insight["color"]};padding:0.8em;border-radius:5px;margin-bottom:10px;color:#000;'>
            {insight["text"]}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("건강수명 vs 기대수명")
        
        # 바 차트: 건강수명 vs 기대수명
        fig = px.bar(
            life_expectancy_data,
            x="국가",
            y=["건강수명", "기대수명"],
            barmode="group",
            color_discrete_map={"건강수명": colors["success"], "기대수명": colors["primary"]},
            labels={"value": "연수", "variable": "구분"},
            title="국가별 건강수명과 기대수명 비교"
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    # 걷기 효과 요약
    st.subheader("걷기의 주요 효과")
    
    effects_col1, effects_col2, effects_col3, effects_col4 = st.columns(4)
    
    with effects_col1:
        st.markdown("""
        <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;color:#000;'>
        <h3 style='color:#1565C0;font-size:1.2em'>근육 건강</h3>
        <p style='font-size:0.9em;'>하반신 근육 강화를 통한 균형감각 향상 및 낙상 위험 감소</p>
        </div>
        """, unsafe_allow_html=True)
    
    with effects_col2:
        st.markdown("""
        <div style='background-color:#E8F5E9;padding:1em;border-radius:10px;color:#000;'>
        <h3 style='color:#2E7D32;font-size:1.2em'>뇌 건강</h3>
        <p style='font-size:0.9em;'>마이오카인 생성을 통한 치매, 알츠하이머 위험 감소</p>
        </div>
        """, unsafe_allow_html=True)
    
    with effects_col3:
        st.markdown("""
        <div style='background-color:#F3E5F5;padding:1em;border-radius:10px;color:#000;'>
        <h3 style='color:#7B1FA2;font-size:1.2em'>혈관 건강</h3>
        <p style='font-size:0.9em;'>모세혈관 소실 방지 및 혈압, 혈당 조절 개선</p>
        </div>
        """, unsafe_allow_html=True)
    
    with effects_col4:
        st.markdown("""
        <div style='background-color:#FFF8E1;padding:1em;border-radius:10px;color:#000;'>
        <h3 style='color:#F57F17;font-size:1.2em'>정신 건강</h3>
        <p style='font-size:0.9em;'>우울증 예방 및 스트레스 감소 효과</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 노화 상태 체크
    st.markdown("---")
    st.subheader("노화 상태 체크")
    
    st.markdown("""
    <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;color:#000;'>
    <h3 style='color:#1565C0;font-size:1.2em'>눈 뜨고 한 발 서기 테스트</h3>
    <p>65세 평균: <strong>50초</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    test_col1, test_col2 = st.columns([2, 1])
    
    with test_col1:
        st.markdown("""
        <ol style='color:#000;'>
          <li>한쪽 발을 들어 올린 상태에서 균형을 유지합니다</li>
          <li>눈을 뜬 채로 최대한 오래 버팁니다</li>
          <li>균형을 잃는 순간 시간을 기록합니다</li>
          <li>양쪽 발로 3회씩 측정하여 평균값을 구합니다</li>
        </ol>
        """, unsafe_allow_html=True)
    
    with test_col2:
        seconds = st.number_input("당신의 결과 (초)", min_value=0, max_value=120, value=0, step=1)
        if st.button("결과 확인"):
            threshold = 50
            if seconds >= threshold:
                st.success(f"훌륭합니다! 65세 평균({threshold}초)보다 {seconds - threshold}초 더 오래 유지했습니다.")
            elif seconds > 0:
                st.warning(f"65세 평균({threshold}초)보다 {threshold - seconds}초 부족합니다. 걷기 운동을 통해 균형감각을 향상시켜 보세요.")

# 걷기 효과 페이지
elif page == "걷기 효과":
    st.title("걷기의 건강상 효과")
    
    st.markdown("""
    <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;color:#000;'>
    규칙적인 걷기는 다양한 질환의 위험을 감소시키고 건강 수명을 연장하는 데 도움이 됩니다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 도넛 차트와 막대 차트를 두 컬럼으로 나누기
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("질환별 위험 감소율")
        
        fig = px.pie(
            walking_benefits_data,
            names="질환",
            values="위험감소율(%)",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2,
            title="걷기를 통한 질환별 위험 감소율 (%)"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("연령대별 권장 걷기 시간")
        
        fig = px.bar(
            age_walking_time_data,
            x="연령대",
            y="권장시간(분)",
            color="권장시간(분)",
            color_continuous_scale=px.colors.sequential.Blues,
            labels={"권장시간(분)": "권장 시간 (분/일)"},
            title="연령대별 권장 걷기 시간 (분/일)"
        )
        fig.update_layout(
            coloraxis_showscale=False,
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 마이오카인 효과와 시간대별 효과를 두 컬럼으로 나누기
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("마이오카인의 건강 효과")
        
        st.markdown("""
        <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;margin-bottom:1em;color:#000;'>
        <h3 style='color:#1565C0;font-size:1.2em'>마이오카인이란?</h3>
        <p>근육 운동 시 근육에서 분비되는 물질로, 다양한 건강상 이점을 제공합니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        effects_col1, effects_col2 = st.columns(2)
        
        with effects_col1:
            st.markdown("""
            <div style='border:1px solid #BBDEFB;padding:0.8em;border-radius:5px;margin-bottom:10px;color:#000;'>
            <h4 style='color:#1565C0;font-size:1em;margin-bottom:0.3em;'>뇌 건강</h4>
            <p style='font-size:0.8em;'>치매, 알츠하이머병 위험 감소</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='border:1px solid #BBDEFB;padding:0.8em;border-radius:5px;margin-bottom:10px;color:#000;'>
            <h4 style='color:#1565C0;font-size:1em;margin-bottom:0.3em;'>심혈관 건강</h4>
            <p style='font-size:0.8em;'>심혈관 질환 및 뇌졸중 위험 감소</p>
            </div>
            """, unsafe_allow_html=True)
        
        with effects_col2:
            st.markdown("""
            <div style='border:1px solid #BBDEFB;padding:0.8em;border-radius:5px;margin-bottom:10px;color:#000;'>
            <h4 style='color:#1565C0;font-size:1em;margin-bottom:0.3em;'>정신 건강</h4>
            <p style='font-size:0.8em;'>우울증 예방 및 스트레스 감소</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='border:1px solid #BBDEFB;padding:0.8em;border-radius:5px;margin-bottom:10px;color:#000;'>
            <h4 style='color:#1565C0;font-size:1em;margin-bottom:0.3em;'>대사 건강</h4>
            <p style='font-size:0.8em;'>인슐린 감수성 향상 및 혈당 조절</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col4:
        st.subheader("시간대별 걷기 효과")
        
        st.markdown("""
        <div style='background-color:#FFF8E1;padding:1em;border-radius:10px;margin-bottom:1em;color:#000;'>
        <p>연구 결과에 따르면 <strong>16~18시에 걷는 것</strong>이 혈당조절과 심혈관건강에 가장 효과적입니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 라인 차트: 시간대별 효과
        fig = px.line(
            time_effect_data,
            x="시간대",
            y=["혈당조절효과", "심혈관건강효과"],
            markers=True,
            color_discrete_map={"혈당조절효과": colors["primary"], "심혈관건강효과": colors["success"]},
            labels={"value": "효과 점수", "variable": "효과 유형"},
            title="시간대별 걷기 효과 비교"
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

# 걷기 방법 페이지
elif page == "걷기 방법":
    st.title("다양한 걷기 방법")
    
    st.markdown("""
    <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;color:#000;'>
    목적과 체력에 맞는 걷기 방법을 선택하여 실천해보세요.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 방법별 레이더 차트
    st.subheader("걷기 종류별 효과 비교")
    
    # 레이더 차트용 데이터 준비
    categories = ['심폐지구력', '근력강화', '스트레스감소', '혈당조절']
    
    fig = go.Figure()
    
    for i, method in walking_methods.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=[method['심폐지구력'], method['근력강화'], method['스트레스감소'], method['혈당조절']],
            theta=categories,
            fill='toself',
            name=method['방법']
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 방법별 상세 설명
    st.subheader("방법별 상세 설명")
    
    for i, method in walking_methods.iterrows():
        with st.expander(f"{method['방법']}", expanded=i==0):
            method_col1, method_col2 = st.columns([3, 2])
            
            with method_col1:
                st.markdown(f"### {method['방법']}")
                st.markdown(f"**설명**: {method['설명']}")
                st.markdown(f"**실천방법**: {method['실천방법']}")
            
            with method_col2:
                # 효과 게이지 표시
                st.markdown("#### 효과")
                
                st.markdown(f"심폐지구력: {method['심폐지구력']}%")
                st.progress(method['심폐지구력']/100)
                
                st.markdown(f"근력강화: {method['근력강화']}%")
                st.progress(method['근력강화']/100)
                
                st.markdown(f"스트레스감소: {method['스트레스감소']}%")
                st.progress(method['스트레스감소']/100)
                
                st.markdown(f"혈당조절: {method['혈당조절']}%")
                st.progress(method['혈당조절']/100)
    
    # 노화 상태 체크
    st.markdown("---")
    st.subheader("노화 상태 체크")
    
    check_col1, check_col2 = st.columns([2, 1])
    
    with check_col1:
        st.markdown("""
        <div style='background-color:#E3F2FD;padding:1.2em;border-radius:10px;height:100%;color:#000;'>
        <h3 style='color:#1565C0;font-size:1.2em'>눈 뜨고 한 발 서기 테스트</h3>
        <p>65세 평균: <strong>50초</strong></p>
        <ol style='color:#000;'>
          <li>한쪽 발을 들어 올린 상태에서 균형을 유지합니다</li>
          <li>눈을 뜬 채로 최대한 오래 버팁니다</li>
          <li>균형을 잃는 순간 시간을 기록합니다</li>
          <li>양쪽 발로 3회씩 측정하여 평균값을 구합니다</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with check_col2:
        seconds = st.number_input("당신의 결과 (초)", min_value=0, max_value=120, value=0, step=1, key="test_result2")
        if st.button("결과 확인", key="check_button2"):
            threshold = 50
            if seconds >= threshold:
                st.success(f"훌륭합니다! 65세 평균({threshold}초)보다 {seconds - threshold}초 더 오래 유지했습니다.")
            elif seconds > 0:
                st.warning(f"65세 평균({threshold}초)보다 {threshold - seconds}초 부족합니다. 걷기 운동을 통해 균형감각을 향상시켜 보세요.")

# 생활 지침 페이지
elif page == "생활 지침":
    st.title("일상 생활 속 걷기 지침")
    
    st.markdown("""
    <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;color:#000;'>
    걷기를 일상 생활에 자연스럽게 통합하는 방법을 알아보세요.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 일일 생활 지침과 영양소 정보를 두 컬럼으로 나누기
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("일일 생활 지침")
        
        for i, row in lifestyle_guidelines.iterrows():
            st.markdown(f"""
            <div style='background-color:#E3F2FD;padding:1em;border-radius:10px;margin-bottom:1em;color:#000;'>
            <h3 style='color:#1565C0;font-size:1.2em'>{row['시간대']}</h3>
            <p>{row['내용']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("도움이 되는 영양소")
        
        st.markdown("걷기 운동의 효과를 높이기 위해 다음 영양소를 함께 섭취하는 것이 좋습니다:")
        
        for i, row in nutrition_data.iterrows():
            st.markdown(f"""
            <div style='border:1px solid #BBDEFB;padding:0.8em;border-radius:5px;margin-bottom:0.8em;color:#000;'>
            <h4 style='color:#1565C0;font-size:1em;margin-bottom:0.3em;'>{row['영양소']}</h4>
            <p style='font-size:0.9em;'>{row['효과']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background-color:#FFF8E1;padding:1em;border-radius:10px;margin-top:1em;color:#000;'>
        <h3 style='color:#F57F17;font-size:1.2em'>걷기 좋은 시간대</h3>
        <p>연구결과에 따르면 16~18시에 걷는 것이 혈당조절과 심혈관건강에 더 효과적입니다.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 걷기 전후 체크리스트
    st.markdown("---")
    st.subheader("걷기 전후 체크리스트")
    
    check_col1, check_col2 = st.columns(2)
    
    with check_col1:
        st.markdown("""
        <div style='background-color:#E3F2FD;padding:1.2em;border-radius:10px;height:100%;color:#000;'>
        <h3 style='color:#1565C0;font-size:1.2em'>걷기 전</h3>
        <ul style='padding-left:1.5em;color:#000;'>
          <li>혈압 체크하기</li>
          <li>식후 1시간이 지난 후 걷기</li>
          <li>적절한 신발과 의복 준비</li>
          <li>충분한 수분 섭취</li>
          <li>스트레칭으로 몸 풀기</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with check_col2:
        st.markdown("""
        <div style='background-color:#E8F5E9;padding:1.2em;border-radius:10px;height:100%;color:#000;'>
        <h3 style='color:#2E7D32;font-size:1.2em'>걷기 후</h3>
        <ul style='padding-left:1.5em;color:#000;'>
          <li>채소 섭취하기</li>
          <li>가벼운 스트레칭</li>
          <li>수분 보충하기</li>
          <li>걸은 시간과 거리 기록하기</li>
          <li>충분한 휴식 취하기</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
