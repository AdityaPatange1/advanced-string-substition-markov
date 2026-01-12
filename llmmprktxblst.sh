#!/bin/bash
# LLM Manipuraka Text Blast - Powered by Sadhguru Shri Brahma
# Transforms every word into random Sanskrit/Chakra words

# 117 Chakra and Sanskrit words dictionary
DICTIONARY=(
    "Muladhara" "Svadhisthana" "Manipura" "Anahata" "Vishuddha" "Ajna" "Sahasrara"
    "Kundalini" "Prana" "Shakti" "Shiva" "Brahman" "Atman" "Dharma" "Karma"
    "Chakra" "Nadi" "Sushumna" "Ida" "Pingala" "Bindu" "Ojas" "Tejas" "Agni"
    "Vayu" "Akasha" "Prithvi" "Apas" "Jala" "Tattva" "Guna" "Sattva" "Rajas"
    "Tamas" "Maya" "Prakriti" "Purusha" "Samadhi" "Dhyana" "Dharana" "Pratyahara"
    "Pranayama" "Asana" "Yama" "Niyama" "Bandha" "Mudra" "Mantra" "Yantra"
    "Tantra" "Vedanta" "Samkhya" "Yoga" "Bhakti" "Jnana" "Kriya" "Raja"
    "Hatha" "Laya" "Nada" "Shabda" "Spanda" "Vikalpa" "Nirvikalpa" "Turiya"
    "Jagrat" "Svapna" "Sushupti" "Ananda" "Chit" "Sat" "Vidya" "Avidya"
    "Moksha" "Nirvana" "Kaivalya" "Jivanmukti" "Siddhi" "Vibhuti" "Avadhuta"
    "Paramahansa" "Sadguru" "Diksha" "Shaktipat" "Samskara" "Vasana" "Chitta"
    "Manas" "Buddhi" "Ahamkara" "Antahkarana" "Kosha" "Annamaya" "Pranamaya"
    "Manomaya" "Vijnanamaya" "Anandamaya" "Linga" "Sharira" "Sthula" "Sukshma"
    "Karana" "Bhuta" "Indriya" "Kleshas" "Sankalpa" "Tapas" "Svadhyaya"
    "Ishvara" "Pranidhana" "Abhyasa" "Vairagya" "Viveka" "Vichara" "Nirodha"
    "Ekagrata" "Samprajnata" "Asamprajnata" "Sabija" "Nirbija"
)

DICT_SIZE=${#DICTIONARY[@]}
INPUT_FILE="sample_text_for_testing.txt"

if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: $INPUT_FILE not found!"
    exit 1
fi

# Read file and transform each word
transformed=""
while IFS= read -r line || [[ -n "$line" ]]; do
    new_line=""
    for word in $line; do
        # Get random index
        random_index=$((RANDOM % DICT_SIZE))
        random_word="${DICTIONARY[$random_index]}"

        # Preserve punctuation at end of word
        punctuation=""
        if [[ "$word" =~ [[:punct:]]$ ]]; then
            punctuation="${word: -1}"
            word="${word%?}"
        fi

        if [[ -n "$new_line" ]]; then
            new_line="$new_line $random_word$punctuation"
        else
            new_line="$random_word$punctuation"
        fi
    done
    transformed+="$new_line"$'\n'
done < "$INPUT_FILE"

# Write back to original file
echo -n "$transformed" > "$INPUT_FILE"

echo "Manipuraka Text Blast Complete!"
echo "All words transformed to Sanskrit/Chakra terminology."
echo "Powered by Sadhguru Shri Brahma"
