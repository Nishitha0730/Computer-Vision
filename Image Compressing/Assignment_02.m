I = imread('Downloaded_Images/lena.jpg');       
I = double(I);                 % Convert to double 
[M, N] = size(I);


figure; imshow(uint8(I));
title('Original Image');


%% Define standard quantization matrix (Q50)
Q50 = [
    16 11 10 16 24 40 51 61;
    12 12 14 19 26 58 60 55;
    14 13 16 24 40 57 69 56;
    14 17 22 29 51 87 80 62;
    18 22 37 56 68 109 103 77;
    24 35 55 64 81 104 113 92;
    49 64 78 87 103 121 120 101;
    72 92 95 98 112 100 103 99];

% Define quality levels 
quality_levels = [60,30,10];


%% 3. Process for each quality level
for q = 1:length(quality_levels)
    
    quality = quality_levels(q);
    
    
    if quality > 50
        scale = (100 - quality) / 50;
    else
        scale = 50 / quality;
    end
    Q = round(Q50 * scale);
    Q(Q==0) = 1;    % Avoid division by zero
    
    %% Level-off 
    I_shifted = I - 128;
    
    %% Divide into 8x8 blocks
    blocks = mat2cell(I_shifted, 8*ones(1, M/8), 8*ones(1, N/8));
    
    %% Apply DCT and Quantization to each block
    blocks_DCT = cell(size(blocks));
    blocks_quantized = cell(size(blocks));
    zero_count = 0;
    total_elements = 0;
    
    for i = 1:size(blocks,1)
        for j = 1:size(blocks,2)
            B = blocks{i,j};
            C = dct2(B);                  % Apply 2D DCT
            S = round(C ./ Q);            % Quantization
            blocks_DCT{i,j} = C;
            blocks_quantized{i,j} = S;
            
            % Count zeros
            zero_count = zero_count + sum(S(:) == 0);
            total_elements = total_elements + numel(S);
        end
    end
    
    %% Dequantization and IDCT
    blocks_reconstructed = cell(size(blocks));
    
    for i = 1:size(blocks,1)
        for j = 1:size(blocks,2)
            S = blocks_quantized{i,j};
            R = S .* Q;                   % Dequantization
            E = idct2(R);                 % Inverse DCT
            blocks_reconstructed{i,j} = E;
        end
    end
    
    %% Combine all 8x8 blocks
    I_rec_shifted = cell2mat(blocks_reconstructed);
    
    %% Add 128 back to reconstruct image
    I_rec = I_rec_shifted + 128;
    I_rec = min(max(I_rec, 0), 255);     % Clamp pixel values
    
    %% Compute PSNR
    MSE = mean(mean((I - I_rec).^2));
    PSNR = 20 * log10(255 / sqrt(MSE));
    
    %% Compute percentage of zeros
    ZeroPercentage = (zero_count / total_elements) * 100;
    
    % Save results
    PSNR_values(q) = PSNR;
    ZeroPerc(q) = ZeroPercentage;
    
    %% Display results
    figure;
    imshow(uint8(I_rec));

    % Save images
    filename = sprintf('Parrots_%03d.jpg', q);
    full_path = fullfile('Results','Parrots', filename);
    imwrite(mat2gray(I_rec), full_path);
    

    title(sprintf('Quality Level = %d | PSNR = %.2f dB | Zeros = %.2f%%', ...
        quality, PSNR, ZeroPercentage));
    
end

%% Summary of results
fprintf('\n----------------------------------------\n');
fprintf(' Quality |   PSNR (dB)   |  Zero %% \n');
fprintf('----------------------------------------\n');
for k = 1:length(quality_levels)
    fprintf('   %3d   |   %8.2f   |  %6.2f%%\n', ...
        quality_levels(k), PSNR_values(k), ZeroPerc(k));
end
fprintf('----------------------------------------\n');

%% Plot PSNR vs Quality
figure;
plot(quality_levels, PSNR_values, '-o', 'LineWidth', 2);
xlabel('Quality Level');
ylabel('PSNR (dB)');
title('PSNR vs Quality Level');
grid on;

