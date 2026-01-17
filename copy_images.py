import shutil
import os

source_dir = r"C:\Users\elwru\.gemini\antigravity\brain\13aa495e-b672-4c1c-a2f7-5bf538915389"
target_dir = r"c:\PROJECTS\LESSONS AND SLIDESHOWS 2\18-01-26_Fight-or-Flight\images"

mapping = {
    "brain_alarm_1768690917377.png": "brain_alarm.png",
    "body_scan_1768690935895.png": "body_scan.png",
    "cat_alert_1768690950018.png": "cat_alert.png",
    "warning_lights_1768690964400.png": "warning_lights.png",
    "baby_bird_instinct_1768690979996.png": "baby_bird_instinct.png",
    "hormones_messengers_1768691000829.png": "hormones_messengers.png",
    "adrenaline_bolt_1768691017618.png": "adrenaline_bolt.png",
    "glucose_energy_1768691034293.png": "glucose_energy.png",
    "organs_blueprint_1768691047086.png": "organs_blueprint.png",
    "fact_hunt_scan_1768691061171.png": "fact_hunt_scan.png",
    "vocab_sync_wires_1768691075953.png": "vocab_sync_wires.png"
}

for src_name, tgt_name in mapping.items():
    src_path = os.path.join(source_dir, src_name)
    tgt_path = os.path.join(target_dir, tgt_name)
    shutil.copy2(src_path, tgt_path)
    print(f"Copied {src_name} to {tgt_name}")
