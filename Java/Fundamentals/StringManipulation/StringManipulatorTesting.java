class StringManipulatorTesting {
    public static void main(String[] args) {
        StringManipulator output = new StringManipulator();
        String getString1 = output.trimAndConcat("Hello ", "World ");
        System.out.println(getString1);

        String getString2 = output.getIndexOrNull("Hello", 'e');
        System.out.println(getString2);

        String getString3 = output.getIndexOrNull("Hello", "lo");
        System.out.println(getString3);

        String getString4 = output.concatSubstring("Hello", 2, 4, "World");
        System.out.println(getString4);
    }
}
