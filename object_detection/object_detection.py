from config import *

# TBA: Ads, intermediate currency,  checkbox selected
object_classes = ["LIKE", "DISLIKE", "STAR", "TSON", "AD", "ADLOADER"]
map_obj_detection_dp = {
    "LIKE": [class_dp["nagging"]]
    , "DISLIKE": [class_dp["nagging"]]
    , "STAR": [class_dp["nagging"]]
    , "TSON": [class_dp["default_choice"]]
    , "AD": [class_dp["nagging"], class_dp["bait_and_switch"], class_dp["disguised_ads"]]
    , "ADLOADER": [class_dp["nagging"], class_dp["gamification"]]
}

def get_inference_result(filename):
    # read the JSON from the object detection result
    pass

def get_potential_dp_classes(label):
    object_class = object_classes[label]
    return map_obj_detection_dp[object_class]

def get_object_detection_result():
    # get_inference_result(filename)
    # get_potential_dp_classes(label)
    object_detection_results = {
        "boxes": [35.015377044677734, 693.7750854492188, 1080.0, 1903.0919189453125]
        , "labels": 1
        , "scores": 0.11882354319095612}
    return object_detection_results

# print("================= INFERENCE ===========================")
# with torch.no_grad():
#     correct = 0
#     total = 0
#     for images, labels in data_loader_test:
#         print("-------batch------------")
#         # pp.pprint(labels)
#         outputs = model(images)
#         print("boxes")
#         pp.pprint(outputs[0]["boxes"][0].numpy().tolist())
#         print("labels")
#         pp.pprint(outputs[0]["labels"][0].numpy().tolist())
#         print("scores")
#         pp.pprint(outputs[0]["scores"][0].numpy().tolist())
#         break
#
# ================= INFERENCE ===========================
# -------batch------------
# boxes
# [35.015377044677734, 693.7750854492188, 1080.0, 1903.0919189453125]
# labels
# 1
# scores
# 0.11882354319095612
