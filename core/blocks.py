from wagtail.core import blocks
from wagtailcodeblock.blocks import CodeBlock
from wagtail.core.blocks import StreamBlock


class RichTextBlock(blocks.RichTextBlock):
    """
    Custom rich text editor based on Wagtail's RichTextBlock
    """
    class Meta:
        template = "core/blocks/rich_text_block.html"
        icon = "doc_full"
        label = "Editor"


class CodeStreamBlock(StreamBlock):
    """
    Test StreamBlock with a CodeBlock.
    """
    code = CodeBlock()
