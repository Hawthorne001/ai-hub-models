# ---------------------------------------------------------------------
# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from qai_hub_models.models._shared.llm.evaluate import llm_evaluate
from qai_hub_models.models.llama_v3_taide_8b_chat import FP_Model, Model

if __name__ == "__main__":
    llm_evaluate(quantized_model_cls=Model, fp_model_cls=FP_Model)
