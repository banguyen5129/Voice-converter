original= 'originalFMvoice.wav';
output = 'analysisFMvoice.wav';
[signal_org,sf] = audioread(original);
[signal_out,sf1] = audioread(output);

figure;

subplot(2,1,1);
i = 1:length(signal_org);
t = i/sf;

plot(t, signal_org);
title("original waveform");
xlabel("time(s)");
ylabel("magnitude");
subplot(2,1,2);
i=1:length(signal_out);
t = i/sf1;
plot(t,signal_out);
title("synthesised waveform"); 
xlabel("time(s)");
ylabel("magnitude");
% Fs = sf;
% N = length(signal_org);
% xdft = fft(signal_org);
% xdft = xdft(1:N/2+1);
% psdx = (1/(Fs*N)) * abs(xdft).^2;
% psdx(2:end-1) = 2*psdx(2:end-1);
% freq = 0:Fs/length(signal_org):Fs/2;

% plot(freq,10*log10(psdx))
% grid on
% title('Periodogram Using FFT')
% xlabel('Frequency (Hz)')
% ylabel('Power/Frequency (dB/Hz)')
% 
% figure;
% Fs = sf1;
% N = length(signal_out);
% xdft = fft(signal_out);
% xdft = xdft(1:N/2+1);
% psdx = (1/(Fs*N)) * abs(xdft).^2;
% psdx(2:end-1) = 2*psdx(2:end-1);
% freq = 0:Fs/length(signal_out):Fs/2;
% 
% plot(freq,10*log10(psdx))
% grid on
% title('Periodogram Using FFT')
% xlabel('Frequency (Hz)')
% ylabel('Power/Frequency (dB/Hz)')
figure('Name','original speech');
spectrogram(signal_org);
title("Original Speech Frequency Domain");
view(-45,65);
figure('Name','synthesized speech');
spectrogram(signal_out);
view(-45,65);
title("Synthesised Speech Frequency Domain");