"use client";
import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";
import Bold from "@tiptap/extension-bold";
import Italic from "@tiptap/extension-italic";
import Underline from "@tiptap/extension-underline";
import BulletList from "@tiptap/extension-bullet-list";
import OrderedList from "@tiptap/extension-ordered-list";
import ListItem from "@tiptap/extension-list-item";

export default function RichTextEditor({ value, onChange }) {
  const editor = useEditor({
    extensions: [
      StarterKit,// desactivamos el history propio
      Bold,
      Italic,
      Underline,
      BulletList,
      OrderedList,
      ListItem,
    ],
    content: value || "<p><Escribe la preparación de la receta...></p>",
    onUpdate: ({ editor }) => onChange(editor.getHTML()),
  });

  if (!editor) return null;

  return (
    <div className="richtext-editor">
      <div className="toolbar">
        <button type="button" onClick={() => editor.chain().focus().toggleBold().run()} className={`btn-bold ${editor.isActive("bold") ? "active" : ""}`}>B</button>
        <button type="button" onClick={() => editor.chain().focus().toggleItalic().run()} className={`btn-italic ${editor.isActive("italic") ? "active" : ""}`}>I</button>
        <button type="button" onClick={() => editor.chain().focus().toggleUnderline().run()} className={`btn-underline ${editor.isActive("underline") ? "active" : ""}`}>U</button>

        <button type="button" onClick={() => editor.chain().focus().setParagraph().run()} className={editor.isActive("paragraph") ? "active" : ""}>p</button>
        <button type="button" onClick={() => editor.chain().focus().toggleHeading({ level: 1 }).run()} className={editor.isActive("heading", { level: 1 }) ? "active" : ""}>H1</button>
        <button type="button" onClick={() => editor.chain().focus().toggleHeading({ level: 2 }).run()} className={editor.isActive("heading", { level: 2 }) ? "active" : ""}>h2</button>
        <button type="button" onClick={() => editor.chain().focus().toggleHeading({ level: 3 }).run()} className={editor.isActive("heading", { level: 3 }) ? "active" : ""}>h3</button>
        <button type="button" onClick={() => editor.chain().focus().toggleHeading({ level: 4 }).run()} className={editor.isActive("heading", { level: 4 }) ? "active" : ""}>h4</button>

        <button type="button" onClick={() => editor.chain().focus().toggleBulletList().run()} className={editor.isActive("bulletList") ? "active" : ""}>•</button>
        <button type="button" onClick={() => editor.chain().focus().toggleOrderedList().run()} className={editor.isActive("orderedList") ? "active" : ""}>1.</button>

        <button type="button" onClick={() => editor.chain().focus().undo().run()}>↺</button>
        <button type="button" onClick={() => editor.chain().focus().redo().run()}>↻</button>
      </div>

      <div
        className="editor"
        onKeyDown={(event) => {
          if (event.key === "Tab") {
            event.preventDefault();
            if (event.shiftKey) {
              editor.chain().focus().liftListItem("listItem").run();
            } else {
              editor.chain().focus().sinkListItem("listItem").run();
            }
          }
        }}
      >
        <EditorContent editor={editor} />
      </div>
    </div>
  );
}
