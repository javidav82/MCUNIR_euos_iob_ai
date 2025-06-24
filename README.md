# EU OS IOB AI Library

Modular Library for IOB Detection in EU OS.

GitHub Project for the Library:

This annex presents the complete structure of the euos_iob_ai library and the access path to its GitHub repository. The purpose of the library is to detect insider threats (IOBs) within the EU OS operating system. Each component has been developed in Python to facilitate the integration of pre-trained models.

The folder organization reflects the four main stages: event capture, processing, detection, and alert notification. Additionally, it includes a generic model loader and a main entry point to orchestrate the flow.

The folder also contains model files, such as offline-trained artifacts exported for local inference. It features a logging system ready to export alerts both to the console and to syslog in JSON format, facilitating integration with monitoring systems.

The library seeks an optimal balance between efficiency, accuracy, and low resource consumption, validated through an experimental pilot.

GitHub Endpoint:
Each file, its path within the repository, and its functional purpose are detailed below:

euos_iob_ai/config.yaml: Main configuration file.

euos_iob_ai/main.py: Service entry point.

euos_iob_ai/core/monitor.py: Implements the start_monitoring() function.

euos_iob_ai/core/features.py: Contains extract_features(event), which transforms a raw event into a feature vector for inference.

euos_iob_ai/core/dispatcher.py: Includes dispatch_event(event) to sequentially invoke each IOB module.

euos_iob_ai/models/iob_1_offhours.pkl: Pretrained Isolation Forest model.

euos_iob_ai/models/iob_2_privilege.pkl: Pretrained Random Forest model to identify anomalous privilege escalation.
