import streamlit as st

# 1. 페이지 기본 설정 (넓은 화면 레이아웃 적용)
st.set_page_config(
    page_title="MBTI x POKÉMON | 단짝 찾기",
    page_icon="⚡",
    layout="wide"
)

# 2. 다크 & 세련된 네온 글래스모피즘 CSS 스타일 정의
st.markdown("""
    <style>
    /* 전체 배경: 딥 블랙 계열 */
    .stApp {
        background: #090A0F;
        color: #F0F0F0;
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }
    
    /* 포켓몬 로고 컨테이너 */
    .logo-container {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    
    .logo-img {
        max-width: 260px;
        filter: drop-shadow(0 0 15px rgba(245, 158, 11, 0.4));
    }
    
    /* 서브 타이틀 */
    .hero-subtitle {
        font-size: 1.15rem !important;
        color: #9CA3AF;
        text-align: center;
        margin-bottom: 1.8rem;
        font-weight: 400;
    }

    /* 프리미엄 다크 글래스 메인 카드 */
    .pokemon-card {
        background: rgba(22, 27, 38, 0.85);
        border: 1px solid rgba(245, 158, 11, 0.35);
        border-radius: 24px;
        padding: 26px;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9), 0 0 25px rgba(245, 158, 11, 0.15);
    }

    /* 포켓몬 이름 */
    .pokemon-name {
        font-size: 2.2rem !important;
        font-weight: 900;
        color: #FFFFFF;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
    }

    /* 태그 / 서브 텍스트 */
    .type-badge {
        display: inline-block;
        background: rgba(245, 158, 11, 0.15);
        color: #FBBF24;
        border: 1px solid rgba(245, 158, 11, 0.4);
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 16px;
    }

    /* 본문 텍스트 박스 */
    .info-box {
        background: rgba(255, 255, 255, 0.04);
        border-left: 4px solid #F59E0B;
        padding: 14px 18px;
        border-radius: 10px;
        font-size: 1.05rem !important;
        line-height: 1.65;
        color: #E5E7EB;
        margin-top: 12px;
    }

    .info-label {
        color: #FBBF24;
        font-weight: 700;
        margin-bottom: 4px;
        display: block;
    }

    /* 양옆 공통 사이드 카드 스타일 */
    .side-card {
        background: rgba(17, 24, 39, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    .side-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #FBBF24;
        margin-bottom: 12px;
    }

    .side-desc {
        font-size: 0.92rem;
        color: #9CA3AF;
        line-height: 1.5;
        margin-top: 10px;
    }

    /* 입력 폼 라벨 및 선택 상자 다크 커스텀 */
    label {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #F3F4F6 !important;
        margin-bottom: 8px !important;
    }
    
    div[data-baseweb="select"] > div {
        background-color: #111827 !important;
        border: 1px solid #374151 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
    }

    /* 버튼 스타일링 */
    .stButton > button {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #000000 !important;
        font-size: 1.2rem !important;
        font-weight: 800 !important;
        border-radius: 14px !important;
        border: none !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.35) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(245, 158, 11, 0.55) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI별 포켓몬 데이터베이스 (16가지 MBTI)
POKEMON_DATA = {
    "INTP": {
        "ko_name": "후딘",
        "en_name": "Alakazam",
        "type": "에스퍼 (Psychic)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "traits": "IQ 5000의 절대적 지능을 가진 고뇌하는 사색가.",
        "reason": "지식에 대한 끝없는 탐구심과 논리적 지적 호기심을 가진 INTP에게 최고의 지적 파트너가 되어줍니다."
    },
    "INTJ": {
        "ko_name": "뮤츠",
        "en_name": "Mewtwo",
        "type": "에스퍼 (Psychic)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "traits": "냉철한 통찰력과 치밀한 전략적 사고를 가진 강자.",
        "reason": "거대한 비전과 완벽주의를 추구하는 INTJ의 치밀한 전략과 독립적인 성향을 깊이 이해합니다."
    },
    "INFJ": {
        "ko_name": "가디안",
        "en_name": "Gardevoir",
        "type": "에스퍼 / 페어리",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "traits": "마음을 감지하고 깊은 헌신을 바치는 신비로운 수호자.",
        "reason": "타인의 감정에 깊이 공감하고 영적 유대를 중시하는 INFJ와 영혼의 주파수가 완벽히 연결됩니다."
    },
    "INFP": {
        "ko_name": "이브이",
        "en_name": "Eevee",
        "type": "노말 (Normal)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "traits": "무한한 가능성과 다채로운 잠재력을 품은 유연함.",
        "reason": "풍부한 낭만과 무궁무진한 가능성을 가슴에 품고 살아가는 INFP의 든든하고 귀여운 동반자입니다."
    },
    "ISTP": {
        "ko_name": "루카리오",
        "en_name": "Lucario",
        "type": "격투 / 강철",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "traits": "파동을 다루며 상황을 침착하게 해결하는 냉철한 해결사.",
        "reason": "도구를 정교하게 다루고 명확한 문제 해결 능력을 지닌 ISTP와 손발이 척척 맞는 최강의 조합입니다."
    },
    "ISFP": {
        "ko_name": "잠만보",
        "en_name": "Snorlax",
        "type": "노말 (Normal)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "traits": "평화롭고 느긋하게 세상을 즐기는 자유로운 영혼.",
        "reason": "온화하고 현재의 평화로운 순간을 사랑하는 예술가형 ISFP에게 최고의 힐링과 여유를 선사합니다."
    },
    "ISFJ": {
        "ko_name": "해피너스",
        "en_name": "Blissey",
        "type": "노말 (Normal)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "traits": "주변을 진심으로 감싸 안는 따뜻한 보살핌의 아이콘.",
        "reason": "소중한 사람들을 배려하고 아끼는 ISFJ의 헌신적인 따뜻함에 가장 깊은 안식처가 되어줍니다."
    },
    "ISTJ": {
        "ko_name": "거북왕",
        "en_name": "Blastoise",
        "type": "물 (Water)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "traits": "단단한 방패처럼 신뢰감을 주는 묵직한 수호자.",
        "reason": "원칙과 두터운 신의를 최우선으로 여기는 ISTJ에게 절대 무너지지 않는 안정감을 제공합니다."
    },
    "ENTP": {
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "type": "고스트 / 독",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "traits": "예측 불가능한 재치와 유쾌한 장난기를 가진 기획자.",
        "reason": "정형화된 틀을 깨고 독창적인 아이디어를 내놓는 ENTP와 시너지가 터지는 최고의 유쾌한 단짝입니다."
    },
    "ENTJ": {
        "ko_name": "리자몽",
        "en_name": "Charizard",
        "type": "불꽃 / 비행",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "traits": "뜨거운 승부욕과 압도적인 카리스마를 지닌 지도자.",
        "reason": "원대한 목표를 향해 도전하고 정복하는 리더형 ENTJ와 열정의 기운이 완벽히 일치합니다."
    },
    "ENFJ": {
        "ko_name": "망나뇽",
        "en_name": "Dragonite",
        "type": "드래곤 / 비행",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "traits": "다정한 마음으로 타인을 이끄는 선량한 구원자.",
        "reason": "사람들을 독려하고 더 나은 세상을 만들고자 하는 ENFJ의 이타적 리더십에 깊이 응답합니다."
    },
    "ENFP": {
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "type": "전기 (Electric)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "traits": "톡톡 튀는 에너지와 스파크 같은 에너자이저.",
        "reason": "자유롭고 호기심이 샘솟는 ENFP에게 매일매일 새로운 즐거움과 생기를 불어넣어 줍니다."
    },
    "ESTP": {
        "ko_name": "번치코",
        "en_name": "Blaziken",
        "type": "불꽃 / 격투",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png",
        "traits": "순발력과 강렬한 에너지로 전장을 뒤흔드는 모험가.",
        "reason": "스릴을 즐기고 빠르고 화려한 액션을 주도하는 ESTP와 가장 dynamic하게 맞물립니다."
    },
    "ESFP": {
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "type": "노말 / 페어리",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "traits": "스포트라이트를 사랑하는 사랑스러운 분위기 메이커.",
        "reason": "무대의 주인공이 되어 사람들을 매료시키는 ESFP와 함께 세상을 즐겁게 만듭니다."
    },
    "ESFJ": {
        "ko_name": "토게키스",
        "en_name": "Togekiss",
        "type": "페어리 / 비행",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "traits": "행복과 축복의 기운을 퍼뜨리는 사교적인 평화주의자.",
        "reason": "친화력이 뛰어나고 사람들에게 온기를 전하는 ESFJ의 따뜻함에 최고의 호응을 보여줍니다."
    },
    "ESTJ": {
        "ko_name": "윈디",
        "en_name": "Arcanine",
        "type": "불꽃 (Fire)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "traits": "위엄 있는 기품과 굳건한 충성심을 가진 수호신.",
        "reason": "체계적이고 리더십 있게 조직을 관장하는 ESTJ의 곁을 든든하게 지켜주는 자부심입니다."
    }
}

# 4. 3컬럼 화면 레이아웃 (왼쪽 공용아트 | 중앙 메인컨텐츠 | 오른쪽 공용아트)
left_side, main_center, right_side = st.columns([1, 2.2, 1])

# --- [왼쪽 공용 포켓몬 영역] ---
with left_side:
    st.markdown('''
        <div class="side-card">
            <div class="side-title">⭐ STARTER POKÉMON</div>
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png" style="width: 85%; margin: 10px 0;">
            <div class="side-desc">
                <b>모험의 시작을 함께하는 단짝들!</b><br>
                피카츄, 파이리, 꼬북이, 이상해씨처럼 각기 다른 매력을 지닌 포켓몬들이 당신을 기다립니다.
            </div>
        </div>
    ''', unsafe_allow_html=True)

# --- [중앙 메인 컨텐츠 영역] ---
with main_center:
    # 포켓몬 공식 로고
    st.markdown('''
        <div class="logo-container">
            <img class="logo-img" src="https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg" alt="Pokémon Logo">
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="hero-subtitle">나만의 성향(MBTI)과 완벽하게 어울리는 포켓몬 파트너를 찾아보세요!</div>', unsafe_allow_html=True)

    # MBTI 드롭다운 선택
    mbti_list = list(POKEMON_DATA.keys())
    selected_mbti = st.selectbox(
        "SELECT YOUR MBTI TYPE",
        options=mbti_list,
        index=0
    )

    st.write("")

    # 단짝 찾기 버튼
    if st.button("✨ 단짝 포켓몬 매칭하기 ✨", use_container_width=True):
        st.balloons()
        
        p_data = POKEMON_DATA[selected_mbti]
        
        col1, col2 = st.columns([1, 1.1])
        
        with col1:
            st.image(p_data["image"], use_container_width=True)
            
        with col2:
            html_content = f'''<div class="pokemon-card"><div class="pokemon-name">{p_data["ko_name"]}</div><div class="type-badge">{p_data["en_name"]} | {p_data["type"]}</div><div class="info-box"><span class="info-label">⚡ 주요 특징</span>{p_data["traits"]}</div><div class="info-box"><span class="info-label">💛 {selected_mbti} 타입과의 매칭 이유</span>{p_data["reason"]}</div></div>'''
            st.markdown(html_content, unsafe_allow_html=True)

# --- [오른쪽 공용 포켓몬 영역] ---
with right_side:
    st.markdown('''
        <div class="side-card">
            <div class="side-title">🔮 LEGENDARY MATCH</div>
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png" style="width: 85%; margin: 10px 0;">
            <div class="side-desc">
                <b>16가지 MBTI 성향 스펙트럼</b><br>
                당신의 고유한 개성과 주파수가 일치하는 전설 & 환상의 포켓몬 단짝을 지금 바로 확인해보세요.
            </div>
        </div>
    ''', unsafe_allow_html=True)
