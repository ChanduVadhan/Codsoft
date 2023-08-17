import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class WordCountProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter '1' to input text manually, '2' to provide a file path:");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        String text = "";
        if (choice == 1) {
            System.out.println("Enter the text:");
            text = scanner.nextLine();
        } else if (choice == 2) {
            System.out.println("Enter the file path:");
            String filePath = scanner.nextLine();
            text = readTextFromFile(filePath);
        } else {
            System.out.println("Invalid choice.");
            return;
        }
        
        String[] words = text.split("[\\s\\p{Punct}]+");
        int wordCount = words.length;
        
        System.out.println("Total word count: " + wordCount);
        
        // Remove common words (stop words)
        Set<String> stopWords = new HashSet<>(Arrays.asList("the", "and", "is", "in", "to", "a"));
        List<String> filteredWords = new ArrayList<>();
        for (String word : words) {
            if (!stopWords.contains(word.toLowerCase())) {
                filteredWords.add(word);
            }
        }
        
        System.out.println("Word count excluding common words: " + filteredWords.size());
        
        // Word frequency statistics
        Map<String, Integer> wordFrequency = new HashMap<>();
        for (String word : filteredWords) {
            wordFrequency.put(word, wordFrequency.getOrDefault(word, 0) + 1);
        }
        
        System.out.println("Word frequency statistics:");
        for (Map.Entry<String, Integer> entry : wordFrequency.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static String readTextFromFile(String filePath) {
        StringBuilder text = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                text.append(line).append("\n");
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
        return text.toString();
    }
}
