import os
import sys
import subprocess

def download_media(url, download_type):
    # output 디렉토리 생성
    os.makedirs("output", exist_ok=True)
    
    # 기본 yt-dlp 명령어 설정 (출력 경로 지정)
    output_template = "output/%(title)s.%(ext)s"
    
    if "audio" in download_type:
        print("🎵 MP3 음원 추출을 시작합니다...")
        cmd = [
            "yt-dlp",
            "-x", # 오디오만 추출
            "--audio-format", "mp3",
            "--audio-quality", "192K",
            "-o", output_template,
            url
        ]
    else:
        print("🎬 최고화질 영상 다운로드를 시작합니다...")
        cmd = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best", # 최고 화질/음질 병합
            "--merge-output-format", "mp4",
            "-o", output_template,
            url
        ]
        
    # 명령어 실행
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("✅ 다운로드가 성공적으로 완료되었습니다!")
    else:
        print("❌ 다운로드 중 오류가 발생했습니다.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python download.py <URL> <TYPE>")
        sys.exit(1)
        
    youtube_url = sys.argv[1]
    d_type = sys.argv[2]
    
    download_media(youtube_url, d_type)
