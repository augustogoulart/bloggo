from wagtail.core import blocks


class RichTextBlock(blocks.RichTextBlock):
    """
    Custom rich text editor based on Wagtail's RichTextBlock
    """
    class Meta:
        template = "core/blocks/rich_text_block.html"
        icon = "doc_full"
        label = "Editor"

