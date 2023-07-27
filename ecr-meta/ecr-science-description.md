# Science

This plugin uses a ResNet50 transfer learning model to detect snow on the ground at the W083 node at the Bad River in Wisconsin. This can be used to help understand the weather and river conditions in the area.

# AI at the Edge

This plugin takes a picture from the camera (default bottom) and uses the ResNet50 model to return a binary value indicating whether there is snow on the image or not. 


# Inference for Sage Nodes

Anyone can query the plugin output from the Sage data repository, via the `sage_data_client` python library: 
```
# install and import library
import sage_data_client

# query and load data into pandas data frame
df = sage_data_client.query(
    start="-1h",
    filter={
        "plugin": "registry.sagecontinuum.org/arnolda/snow-classifier:0.1.0"
    }
)

# print results in data frame
print(df)

```
For more information, please see [Access and use data documentation](https://docs.sagecontinuum.org/docs/tutorials/accessing-data) and [sage_data_client](https://pypi.org/project/sage-data-client/).