"use client";
import React from "react";
import { useEditor, EditorContent } from "@tiptap/react";
import StarterKit from "@tiptap/starter-kit";

export default function MostrarRichText({ html }) {
  const editor = useEditor({
    editable: false,
    extensions: [
      StarterKit,
    ],
    content: html,
  });
  console.log(editor);

  if (!editor) return <p>Cargando contenido...</p>; 

  return (
    <div className="mostrar-rich-txt">
      <EditorContent editor={editor} />
    </div>
  );
}
