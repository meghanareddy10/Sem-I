# Sem-I
Semantic image inpainting with deep learning experiment with data augmentation in pre processing stage 


Detailed Experiment Overview
--------------------------------------------------

Project Title: Semantic Image Inpainting using Deep Generative Models


Objective
------------
  The primary aim of this project was to investigate the efficacy of a state-of-the-art semantic image inpainting model, specifically the approach proposed by Yeh et al. [1], when          subjected to images that were not part of its original training dataset. The focus was on evaluating the model's performance with images from the Labeled Faces in the Wild (LFW)          dataset, which were both randomly selected and inverted by 180 degrees.

----------------------------------------------

Methodology

1. Model Selection and Pre-training:

  The selected model was based on Yeh et al.'s [1] work, utilizing deep generative models for semantic image inpainting.
  Pre-training was conducted on the CelebA dataset, comprising non-inverted facial images, allowing the model to learn semantic representations and contextual information.
        
2. Dataset Selection for Testing:

  The LFW dataset was chosen for testing due to its diversity and the absence of these images in the model's training set.
  Random LFW images were selected for testing the model's generalization to novel faces and scenarios.

      
3. Image Transformation for Variation:

  To assess the model's robustness, the chosen LFW images were resized to a 64x64 pixel resolution, consistent with the model's training resolution.
  Each image was inverted by 180 degrees, introducing variations in facial feature orientation for a comprehensive evaluation.
        
4. Inpainting Experiment:

   The pre-trained model was applied to inpaint the missing or corrupted regions in the randomly selected and inverted LFW images.
   Inpainting results were qualitatively and quantitatively evaluated to understand the model's capacity to handle diverse inpainting scenarios.
------------------------------------------------------------------------------------------

Results and Observations
-----------------------------
1.Qualitative Analysis:

  *Visual inspection of the inpainted images revealed that while the model did not precisely replicate the original images, it attempted to generate relevant content, maintaining        
   some level of semantic coherence.
  *The inpainting results suggested that the model inferred and inpainted based on the nearest non-inverted images in the latent manifold, showcasing an understanding of contextual          information.
  
2. Quantitative Assessment:

     *Metrics such as Structural Similarity Index (SSI) and Peak Signal-to-Noise Ratio (PSNR) were computed to quantitatively assess the similarity between inpainted and ground truth           images.
     *Results indicated a reasonable level of similarity, although the model did not achieve an exact match, showcasing limitations in handling inverted images.

Find the below image which shows the observations of the experiment-

![image](https://github.com/meghanareddy10/Sem-I/assets/124005410/7826ac21-02a5-4578-af20-a53fad8ed810)


--------------------------------------------------------------------------------------------
Conclusion and Future Work
----------------------------------

The experiment revealed that while the inpaintings did not precisely match the original images when given inverted inputs, the model demonstrated an effort to generate relevant content based on the nearest non-inverted images in the latent manifold. This suggests that the model has limitations in handling inverted images, possibly due to the discrepancy in training data orientation.

For future work, it is recommended to explore strategies to enhance the model's performance on inverted images. This could involve specific training on inverted data or incorporating additional augmentation techniques to improve the model's ability to generalize across diverse inpainting scenarios. Further investigation into understanding and mitigating the challenges posed by inverted inputs will contribute to refining the model's capabilities.
