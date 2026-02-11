import streamlit as st
import yt_dlp
import os
import glob

# 페이지 설정
st.set_page_config(page_title="치지직 영상 다운로더", page_icon="🎬")

st.title("🎬 치지직 영상 다운로더")
st.markdown("다운로드하고 싶은 **치지직 영상(VOD) 주소**를 입력하세요.")

# URL 입력창
url = st.text_input("URL 입력", placeholder="https://chzzk.naver.com/video/...")

if st.button("영상 정보 가져오기"):
    if url:
        try:
            with st.spinner('영상을 분석 중입니다...'):
                # 기존 mp4 파일 삭제 (서버 용량 관리)
                for f in glob.glob("*.mp4"):
                    os.remove(f)

                # yt-dlp 옵션
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': 'downloaded_video.%(ext)s',
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    title = info.get('title', 'video')
                    
                # 다운로드 버튼 생성
                with open("downloaded_video.mp4", "rb") as file:
                    st.success(f"준비 완료: {title}")
                    st.download_button(
                        label="💻 내 컴퓨터로 저장하기",
                        data=file,
                        file_name=f"{title}.mp4",
                        mime="video/mp4"
                    )
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("URL을 입력해주세요.")

st.info("💡 참고: 실시간 라이브 방송은 다시보기가 올라온 후에 다운로드 가능합니다.")
