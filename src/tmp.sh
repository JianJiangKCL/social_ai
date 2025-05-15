MAX_PIXELS=1003520 \
CUDA_VISIBLE_DEVICES=1 \
swift infer \
    --ckpt_dir /data/ckpt/Qwen/Qwen2.5-Omni-3B \
    --val_dataset /data/jj/proj/AFF/data/DSFW/test_set_1.jsonl \
    --result_path /data/jj/proj/AFF/test_output


# bs one 1 maximum
CUDA_VISIBLE_DEVICES=1 \
swift sft \
    --model /data/ckpt/Qwen/Qwen2.5-Omni-3B \
    --train_type lora \
    --dataset /data/jj/proj/AFF/data/DSFW/train_set_1.jsonl \
    --val_dataset /data/jj/proj/AFF/data/DSFW/test_set_1.jsonl \
    --torch_dtype bfloat16 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --output_dir output/ \
    --logging_dir output/ \
    --freeze_vit true \
    --lora_rank 8 \
    --lora_alpha 16 \
    --target_modules all-linear \
    --gradient_checkpointing false \
    --gradient_accumulation_steps 4 \
    --save_strategy "steps" \
    --save_steps 100 \
    --save_total_limit 10 \
    --num_train_epochs  3 \
    --learning_rate 5e-5 \
    --save_only_model false \
    --weight_decay 0.05 \
    --adam_beta2 0.95 \
    --lr_scheduler_type "cosine" \
    --logging_steps 100 \
    --eval_strategy "steps" \
    --eval_steps 500 \
    --warmup_ratio 0.05 \
    --dataset_num_proc 12 \
    --dataloader_num_workers 4 \
    --dataloader_pin_memory true \
    --report_to wandb 