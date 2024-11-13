from tensorflow.keras.models import load_model

# 加载 Keras 模型
model = load_model('Network5x595gamma.h5')

# 打印模型结构
model.summary()
