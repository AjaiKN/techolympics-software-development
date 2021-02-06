# To run this program, run this command: ruby coding5.rb

# To choose the next word, this program looks at the previous word and
# chooses randomly from the words that come after it in both texts.

def get_words
  res = []
  num_newlines_in_a_row = 0
  while num_newlines_in_a_row < 2
    line = gets.chomp
    if line == ""
      num_newlines_in_a_row += 1
    else
      res << line
      num_newlines_in_a_row = 0
    end
  end
  res.join(" ").split(" ").select{|word| word.chomp != ""}
end

puts "End each input text with 2 blank lines."
puts
puts "Text 1:"
words1 = get_words
puts "Text 2:"
words2 = get_words

number_of_words = 0
until number_of_words > 0
  print "Number of words (should be a positive integer): "
  number_of_words = gets.chomp.to_i
end

puts

word_pairs = []
words1.each_cons(2) {|word_pair| word_pairs.push word_pair }
words2.each_cons(2) {|word_pair| word_pairs.push word_pair }

def find_possible_next_words word_pairs, word
  word_pairs.select {|pair| pair[0] == word}.map {|pair| pair[1]}
end

print "Starting word: "
last_word = (gets.chomp + " ").split[0]

for i in 0...number_of_words
  print "#{last_word} "

  possible_next_words = find_possible_next_words(word_pairs, last_word)
  if possible_next_words.length == 0
    last_word = (words1 + words2).sample
  else
    last_word = possible_next_words.sample
  end
end

puts
