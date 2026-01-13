from flask import Flask, request, jsonify
from executor.execute_code import execute_and_capture_output
from analyzer import measure_execution_time, measure_memory

app = Flask(__name__)