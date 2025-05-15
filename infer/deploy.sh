CUDA_VISIBLE_DEVICES=1 \
swift deploy \
    --model /data/ckpt/Qwen/Qwen2.5-Omni-3B \
    --infer_backend vllm \
    --attn_impl flash_attn \
    --gpu_memory_utilization 0.7 \
    --host 0.0.0.0 \
    --port 9000 \
    --served_model_name Qwen2.5-Omni-3B