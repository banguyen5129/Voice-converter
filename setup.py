from cx_Freeze import setup, Executable
import os 
import sys

from encoder.params_model import model_embedding_size as speaker_embedding_size
from utils.argutils import print_args
from utils.modelutils import check_model_paths
from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
from pathlib import Path
import numpy as np
import soundfile as sf
import librosa
import argparse
import torch
import sys
import os
from audioread.exceptions import NoBackendError
import speech_recognition
import tkinter

base = None    

executables = [Executable("demo_cli.py", base=base)]

packages = ["idna", "os", "sys", "utils", "synthesizer", "encoder",                     "vocoder", "pathlib", "numpy", "soundfile", "librosa",                      "argparse", "tkinter", "speech_recognition"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "speech2speech",
    options = options,
    version = "0.0.1",
    description = 'This is speech2speech converter',
    executables = executables
)