# Aruco markers
## Использование маркеров [ArUco](https://docs.opencv.org/3.2.0/d5/dae/tutorial_aruco_detection.html) для навигации в помещении.

### В директории opencv находятся разные скрипты для начала работы с маркерами ArUco:
#### ChessBoard_9x6.jpg
картинка, использующаяся для калибровки камеры
#### save_snapshots.py
скрипт для автоматической съемки и сохранения фото с калибровочной картинкой, потом эти фото используются для калибровки
#### cameracalib.py
скрипт для калибровки камеры, использует фото, полученные с помощью save_snapshots.py
#### cameraDistortion.txt, cameraMatrix.txt
примеры файлов с калибровочной информацией
#### aruco_pose_estimation.py
демонстрация определения положения и ориентации маркера.

Данные скрипты (возможно, с небольшими изменениями) были взяты [здесь](https://github.com/tizianofiorenzani/how_do_drones_work).
Поясняющие видео: [OpenCv and Camera Calibration](https://www.youtube.com/watch?v=QV1a1G4lL3U), [PRECISION LANDING with OPENCV and ARUCO Markers Part 1](https://www.youtube.com/watch?v=wlT_0fhGrGg), [DRONE VISUAL LANDING with Aruco and OpenCv Part 2](https://www.youtube.com/watch?v=iezU2PR0hBk)

#### aruco_distance_demo.py
скрипт для определения направления и рассояния до маркера
Данный скрипт (с изменениями) взят [здесь](https://gist.github.com/horverno/978559e4e3d3cf04ae3dd56ae3d577ec).
 
