import streamlit as st

# 1. 페이지 기본 설정 및 스타일 정의 (크림/노란색 톤, 큰 글씨)
st.set_page_config(
    page_title="MBTI x 포켓몬 단짝 찾기",
    page_icon="⚡",
    layout="centered"
)

# 사용자 지정 CSS 적용
st.markdown("""
    <style>
    /* 배경색 및 기본 폰트 설정 */
    .stApp {
        background-color: #FFFDF0;
        color: #4A3E3D;
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 제목 스타일 */
    .title-text {
        font-size: 2.5rem !important;
        font-weight: 800;
        color: #8B5E3C;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        font-size: 1.3rem !important;
        color: #A07855;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* 카드 스타일 */
    .pokemon-card {
        background-color: #FFFBE6;
        border: 2px solid #FFE58F;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 20px rgba(220, 180, 100, 0.15);
        margin-top: 15px;
    }

    /* 포켓몬 이름 */
    .pokemon-name {
        font-size: 2rem !important;
        font-weight: 800;
        color: #D48806;
        margin-bottom: 5px;
    }

    /* 영어 이름 및 타입 */
    .pokemon-sub {
        font-size: 1.2rem;
        color: #8C6B3F;
        margin-bottom: 15px;
    }

    /* 본문 글자 크기 */
    .info-text {
        font-size: 1.15rem !important;
        line-height: 1.7;
        color: #594A3C;
    }

    /* 셀렉트박스 및 라벨 크기 확대 */
    div[data-baseweb="select"] {
        font-size: 1.2rem !important;
    }
    label {
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        color: #73512F !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. MBTI별 포켓몬 데이터베이스 (16가지 MBTI)
# 이미지는 PokeAPI의 공식 고화질 공식 일러스트 URL을 사용합니다.
POKEMON_DATA = {
    "INTP": {
        "ko_name": "후딘",
        "en_name": "Alakazam",
        "type": "체조 (Psychic)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "traits": "IQ 5000을 자랑하는 절대 지능의 소유자로, 지식을 갈구하고 깊이 생각하는 타입입니다.",
        "reason": "끊임없이 원리를 탐구하고 지적 호기심이 왕성한 INTP와 가장 잘 어울립니다. 분석적이고 독창적인 아이디어를 함께 나누기에 최고의 파트너입니다."
    },
    "INTJ": {
        "ko_name": "뮤츠",
        "en_name": "Mewtwo",
        "type": "에스퍼 (Psychic)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "traits": "냉철한 판단력과 압도적인 전략적 사고를 지닌 고독한 강자입니다.",
        "reason": "장기적인 목표와 완벽성을 추구하는 INTJ의 독립적 성향을 깊이 이해해 줍니다. 서로의 능력을 존중하며 깊은 신뢰를 쌓을 수 있는 단짝입니다."
    },
    "INFJ": {
        "ko_name": "가디안",
        "en_name": "Gardevoir",
        "type": "에스퍼 / 페어리 (Psychic / Fairy)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "traits": "트레이너의 마음을 깊이 감지하고, 미래를 예지하며 끝없는 헌신을 보입니다.",
        "reason": "타인의 감정에 공감하고 통찰력이 뛰어난 INFJ와 영혼의 주파수가 맞춰집니다. 조용하면서도 따뜻한 유대감을 나누기 좋습니다."
    },
    "INFP": {
        "ko_name": "이브이",
        "en_name": "Eevee",
        "type": "노말 (Normal)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "traits": "어떤 환경에서도 무한한 가능성을 품고 성장하는 순수한 포켓몬입니다.",
        "reason": "풍부한 상상력과 가능성을 가슴에 품고 살아가는 INFP와 참 많이 닮았습니다. 나만의 색깔을 찾아가는 여정을 늘 옆에서 응원해 줍니다."
    },
    "ISTP": {
        "ko_name": "루카리오",
        "en_name": "Lucario",
        "type": "격투 / 강철 (Fighting / Steel)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "traits": "상대의 파동(파동)을 감지하며, 정교하고 냉철하게 상황을 해결합니다.",
        "reason": "도구를 잘 다루고 실용적인 문제 해결에 뛰어난 ISTP의 침착함과 어울립니다. 말없이 손발이 척척 맞는 든든한 조력자가 되어줍니다."
    },
    "ISFP": {
        "ko_name": "잠만보",
        "en_name": "Snorlax",
        "type": "노말 (Normal)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "traits": "느긋하고 여유로우며, 세상의 평화로움을 온몸으로 즐기는 포켓몬입니다.",
        "reason": "마음이 따뜻하고 현재의 순간을 소중히 여기는 예술가형 ISFP에게 완벽한 안식처입니다. 함께 누워 쉬는 것만으로도 최고의 힐링을 줍니다."
    },
    "ISFJ": {
        "ko_name": "해피너스",
        "en_name": "Blissey",
        "type": "노말 (Normal)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "traits": "상처받은 이를 진심으로 보살피며 행복을 전파하는 따뜻한 마음을 가졌습니다.",
        "reason": "주변 사람들을 묵묵히 챙기고 배려하는 ISFJ의 헌신적인 성향과 꼭 맞습니다. 서로의 지친 마음을 다정하게 감싸줄 수 있습니다."
    },
    "ISTJ": {
        "ko_name": "거북왕",
        "en_name": "Blastoise",
        "type": "물 (Water)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "traits": "묵직한 껍질처럼 흔들림이 없고, 책임을 다해 동료를 지켜내는 수호자입니다.",
        "reason": "원칙을 지키고 신뢰를 최우선으로 하는 ISTJ에게 최고의 안정감을 선사합니다. 어떤 어려움 속에서도 절대 무너지지 않는 단짝이 됩니다."
    },
    "ENTP": {
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "type": "고스트 / 독 (Ghost / Poison)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "traits": "장난기 넘치고 예측 불가능하며, 언제나 새로운 장난과 아이디어를 냅니다.",
        "reason": "호기심 많고 정형화된 틀을 깨길 좋아하는 ENTP와 시너지가 폭발합니다. 함께 있을 때 지루할 틈이 전혀 없는 최고의 유쾌함을 선사합니다."
    },
    "ENTJ": {
        "ko_name": "리자몽",
        "en_name": "Charizard",
        "type": "불꽃 / 비행 (Fire / Flying)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "traits": "뜨거운 열정과 카리스마로 전장을 지배하며 절대 포기하지 않습니다.",
        "reason": "원대한 목표를 향해 당차게 이끄는 리더형 ENTJ와 열정의 크기가 같습니다. 높은 곳을 향해 함께 도전하고 승리하는 짜릿함을 안겨줍니다."
    },
    "ENFJ": {
        "ko_name": "망나뇽",
        "en_name": "Dragonite",
        "type": "드래곤 / 비행 (Dragon / Flying)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "traits": "넓은 바다를 건너 다친 사람을 돕는 다정하고 선량한 드래곤입니다.",
        "reason": "사람들을 독려하고 더 좋은 세상을 만들고 싶어 하는 ENFJ의 이타심과 통합니다. 선한 영향력을 넓히며 함께 성장할 수 있습니다."
    },
    "ENFP": {
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "type": "전기 (Electric)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "traits": "에너지가 넘치고 방긍방글 밝은 자극을 주는 모두의 인기쟁이입니다.",
        "reason": "재기발랄하고 긍정적인 에너지가 샘솟는 ENFP와 찰떡궁합을 자랑합니다. 어디로 튈지 모르는 스파크 같은 일상을 즐겁게 함께 만들어갑니다."
    },
    "ESTP": {
        "ko_name": "번치코",
        "en_name": "Blaziken",
        "type": "불꽃 / 격투 (Fire / Fighting)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png",
        "traits": "강렬한 도약력과 순발력으로 순간의 모험과 승부를 즐깁니다.",
        "reason": "스릴을 즐기고 순발력이 뛰어난 모험가 ESTP와 다이나믹하게 어우러집니다. 망설임 없이 현장에 몸을 던지는 명쾌함이 잘 맞습니다."
    },
    "ESFP": {
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "type": "노말 / 페어리 (Normal / Fairy)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "traits": "무대의 주인공이 되어 사랑스러운 노래로 사람들의 시선을 사로잡습니다.",
        "reason": "분위기 메이커이자 주목받는 것을 즐기는 ESFP와 조화롭습니다. 함께 무대를 즐기고 언제나 주변을 밝고 즐겁게 만드는 연예인 커플입니다."
    },
    "ESFJ": {
        "ko_name": "토게키스",
        "en_name": "Togekiss",
        "type": "페어리 / 비행 (Fairy / Flying)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "traits": "서로 다투지 않는 은혜로운 곳에 나타나 행복과 축복의 기운을 나누어 줍니다.",
        "reason": "친절하고 친화력이 좋아 모임을 활기차게 만드는 ESFJ의 성향과 어울립니다. 주변 모두에게 따뜻한 기운과 평화를 선물해 줍니다."
    },
    "ESTJ": {
        "ko_name": "윈디",
        "en_name": "Arcanine",
        "type": "불꽃 (Fire)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "traits": "위풍당당한 기품과 위엄을 갖추고 직진하는 신의 깊은 포켓몬입니다.",
        "reason": "조직적이고 결단력 있게 과업을 완수하는 ESTJ의 듬직함을 빼닮았습니다. 명확한 질서와 충성심으로 든든하게 곁을 지켜주는 파트너입니다."
    }
}

# 3. 화면 레이아웃 및 UX 구현
st.markdown('<div class="title-text">⚡ MBTI x 포켓몬 단짝 찾기 ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">나의 MBTI를 선택하고 어울리는 단짝 포켓몬을 만나보세요!</div>', unsafe_allow_html=True)

# MBTI 선택 박스
mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👇 당신의 MBTI 유형을 선택해 주세요:",
    options=mbti_list,
    index=0
)

# 단짝 찾기 버튼
if st.button("✨ 내 단짝 포켓몬 찾아보기 ✨", use_container_width=True):
    # 1) 축하 애니메이션 효과
    st.balloons()
    
    # 선택된 데이터 가져오기
    p_data = POKEMON_DATA[selected_mbti]
    
    # 결과 화면 출력
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        # 포켓몬 고화질 이미지 출력
        st.image(p_data["image"], use_container_width=True)
        
    with col2:
        # 상세 특징 및 어울리는 이유 설명 카드
        st.markdown(f'''
        <div class="pokemon-card">
            <div class="pokemon-name">{p_data["ko_name"]}</div>
            <div class="pokemon-sub"><b>영문명:</b> {p_data["en_name"]} | <b>타입:</b> {p_data["type"]}</div>
            <hr style="border: 0.5px solid #FFE58F; margin: 15px 0;">
            <div class="info-text">
                <b>📌 주요 특징:</b><br>
                {p_data["traits"]}
            </div>
            <br>
            <div class="info-text">
                <b>💛 {selected_mbti}와 잘 어울리는 이유:</b><br>
                {p_data["reason"]}
            </div>
        </div>
        ''', unsafe_allow_html=True)
