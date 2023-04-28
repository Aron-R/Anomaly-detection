import wave

def caesar_cipher_audio(audio_file, shift):
    # Load the audio file
    audio = wave.open(audio_file, mode='rb')

    # Get audio parameters
    nchannels, sampwidth, framerate, nframes, comptype, compname = audio.getparams()

    # Read audio data
    audio_data = audio.readframes(nframes)

    # Convert audio data to bytes
    audio_bytes = bytearray(audio_data)

    # Encrypt the audio data
    for i in range(len(audio_bytes)):
        audio_bytes[i] = (audio_bytes[i] + shift) % 256

    # Save the encrypted audio data to a file
    encrypted_audio_file = f"encrypted_{shift}_{audio_file}"
    with wave.open(encrypted_audio_file, mode='wb') as encrypted_audio:
        encrypted_audio.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
        encrypted_audio.writeframes(audio_bytes)

    # Decrypt the encrypted audio data
    decrypted_audio_file = f"decrypted_{shift}_{audio_file}"
    with wave.open(encrypted_audio_file, mode='rb') as encrypted_audio:
        nchannels, sampwidth, framerate, nframes, comptype, compname = encrypted_audio.getparams()
        encrypted_audio_data = encrypted_audio.readframes(nframes)
        encrypted_audio_bytes = bytearray(encrypted_audio_data)

        # Decrypt the audio data
        for i in range(len(encrypted_audio_bytes)):
            encrypted_audio_bytes[i] = (encrypted_audio_bytes[i] - shift) % 256

        # Save the decrypted audio data to a file
        with wave.open(decrypted_audio_file, mode='wb') as decrypted_audio:
            decrypted_audio.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
            decrypted_audio.writeframes(encrypted_audio_bytes)

    # Display the encrypted and decrypted audio files
    print("Encrypted audio:")
    display(Audio(filename=encrypted_audio_file))
    print("Decrypted audio:")
    display(Audio(filename=decrypted_audio_file))

# Take user input
audio_file = input("Enter audio file path: ")
shift = int(input("Enter shift key: "))

# Encrypt and decrypt the audio file
caesar_cipher_audio(audio_file, shift)