import asyncio
import logging
import json
from aiortc import RTCPeerConnection, RTCSessionDescription, MediaStreamTrack
from aiortc.mediastreams import AudioStreamTrack, VideoStreamTrack
import cv2
import sounddevice as sd
import numpy as np

logging.basicConfig(level=logging.INFO)

class CameraVideoTrack(VideoStreamTrack):
    def __init__(self):
        super().__init__()
        self.camera = cv2.VideoCapture(0)
        
        if not self.camera.isOpened():
            raise RuntimeError("Could not open the camera module.")

    async def recv(self):
        frame_time = await self.next_timestamp()
        ret, frame = self.camera.read()

        if not ret:
            raise RuntimeError("Failed to capture video frame.")

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return VideoFrame.from_ndarray(frame, format="rgb24", timestamp=frame_time)

    def stop(self):
        self.camera.release()

class MicrophoneAudioTrack(AudioStreamTrack):
    def __init__(self):
        super().__init__()
        self.samplerate = 48000
        self.channels = 1
        self.stream = sd.InputStream(samplerate=self.samplerate, channels=self.channels, dtype='int16')
        self.stream.start()

    async def recv(self):
        frame_time = await self.next_timestamp()
        audio_data, _ = self.stream.read(480)
        audio_frame = AudioFrame(data=audio_data.tobytes(), timestamp=frame_time)
        audio_frame.sample_rate = self.samplerate
        audio_frame.channels = self.channels
        return audio_frame

    def stop(self):
        self.stream.stop()
        self.stream.close()

async def create_offer():
    pc = RTCPeerConnection()
    video_track = CameraVideoTrack()
    pc.addTrack(video_track)

    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)

    sdp_dict = {
        'sdp': pc.localDescription.sdp,
        'type': pc.localDescription.type
    }
    sdp_json = json.dumps(sdp_dict)
    return sdp_json

if __name__ == "__main__":
    offer_json = asyncio.run(create_offer())
    print(offer_json)
