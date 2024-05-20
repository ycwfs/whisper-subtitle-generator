import ffmpeg
import subprocess

# def audio_extract(input, output):
# 	ffmpeg.input(input, vn=None).output(output).run()

# 解决中文路径ffmpeg无法运行的问题
def audio_extract(input_path, output_path):
	command = [
		'ffmpeg', 
		'-i', 'pipe:0',  # 从stdin读取输入
		'-vn',          # 仅提取音频
		output_path     # 输出文件路径
	]

	with open(input_path, 'rb') as f:
		subprocess.run(command, input=f.read())

def convert_subtitle(input_path, output_path):
	"""
 	ffmpeg -i puck.srt puck.ass
	"""
	command = [
		'ffmpeg', 
		'-i', input_path,
		output_path
	]

	subprocess.run(command)

def add_subtitle(input_path, output_path, subtitle_path):
	command = [
		'ffmpeg', 
		'-i', input_path,
		'-vf', f"subtitles={subtitle_path}",
		output_path
	]

	subprocess.run(command)