import pickle
import numpy as np
import os


def convert_camera_to_bases_pkl_to_npz(pkl_path="real_world/calibration_result/camera_to_bases.pkl",out_dir="real_world/calibration_result"):
    os.makedirs(out_dir, exist_ok=True)

    camera_to_bases = pickle.load(open(pkl_path, "rb"))

    print("Loaded camera_to_bases.pkl")
    print("Cameras found:", list(camera_to_bases.keys()))
    print()

    for serial, T_cam2base in camera_to_bases.items():
        T_cam2base = np.array(T_cam2base)
        T_base2cam = np.linalg.inv(T_cam2base)

        filename = os.path.join(out_dir, f"camera_{serial}_extrinsics.npz")

        np.savez(
            filename,
            cam2arm=T_cam2base,
            arm2cam=T_base2cam
        )

        print(f"Saved {filename}")
        print("cam2arm:\n", T_cam2base)
        print("arm2cam:\n", T_base2cam)
        print()


if __name__ == "__main__":
    convert_camera_to_bases_pkl_to_npz()
