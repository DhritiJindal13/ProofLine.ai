import React, { useEffect, useState } from 'react'

export default function ResumePreview({ file }) {
  const [previewUrl, setPreviewUrl] = useState(null)

  useEffect(() => {
    if (!file) return
    const url = URL.createObjectURL(file)
    setPreviewUrl(url)
    return () => URL.revokeObjectURL(url)
  }, [file])

  if (!file || !previewUrl) return null

  const linkLabel = "View uploaded resume (" + file.name + ")"

  return React.createElement(
    'a',
    { href: previewUrl, target: '_blank', rel: 'noopener noreferrer', className: 'resume-preview-link' },
    linkLabel
  )
}
