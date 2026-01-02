from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, field_validator, BeforeValidator
from src.models.RomFileSchema import RomFileSchema
from src.models.RomFlashpointMetadata import RomFlashpointMetadata
from src.models.RomGamelistMetadata import RomGamelistMetadata
from src.models.RomHLTBMetadata import RomHLTBMetadata
from src.models.RomHasheousMetadata import RomHasheousMetadata
from src.models.RomIGDBMetadata import RomIGDBMetadata
from src.models.RomLaunchboxMetadata import RomLaunchboxMetadata
from src.models.RomMetadataSchema import RomMetadataSchema
from src.models.RomMobyMetadata import RomMobyMetadata
from src.models.RomRAMetadata import RomRAMetadata
from src.models.RomSSMetadata import RomSSMetadata
from src.models.RomUserSchema import RomUserSchema
from src.models.SiblingRomSchema import SiblingRomSchema
from src.validators.modelValidators import empty_dict_to_none


class SimpleRomSchema(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    igdb_id: int | None
    sgdb_id: int | None
    moby_id: int | None
    ss_id: int | None
    ra_id: int | None
    launchbox_id: int | None
    hasheous_id: int | None
    tgdb_id: int | None
    flashpoint_id: str | None
    hltb_id: int | None
    gamelist_id: str | None
    platform_id: int
    platform_slug: str
    platform_fs_slug: str
    platform_custom_name: str | None
    platform_display_name: str
    fs_name: str
    fs_name_no_tags: str
    fs_name_no_ext: str
    fs_extension: str
    fs_path: str
    fs_size_bytes: int
    name: str | None
    slug: str | None
    summary: str | None
    alternative_names: list[str]
    youtube_video_id: str | None
    metadatum: RomMetadataSchema
    igdb_metadata: Annotated[RomIGDBMetadata | None, BeforeValidator(empty_dict_to_none)]
    moby_metadata: Annotated[RomMobyMetadata | None, BeforeValidator(empty_dict_to_none)]
    ss_metadata: Annotated[RomSSMetadata | None, BeforeValidator(empty_dict_to_none)]
    launchbox_metadata: Annotated[RomLaunchboxMetadata | None, BeforeValidator(empty_dict_to_none)]
    hasheous_metadata: Annotated[RomHasheousMetadata | None, BeforeValidator(empty_dict_to_none)]
    flashpoint_metadata: Annotated[RomFlashpointMetadata | None, BeforeValidator(empty_dict_to_none)]
    hltb_metadata: Annotated[RomHLTBMetadata | None, BeforeValidator(empty_dict_to_none)]
    gamelist_metadata: Annotated[RomGamelistMetadata | None, BeforeValidator(empty_dict_to_none)]
    path_cover_small: str | None
    path_cover_large: str | None
    url_cover: str | None
    has_manual: bool
    path_manual: str | None
    url_manual: str | None
    is_identifying: bool = False
    is_unidentified: bool
    is_identified: bool
    revision: str | None
    regions: list[str]
    languages: list[str]
    tags: list[str]
    crc_hash: str | None
    md5_hash: str | None
    sha1_hash: str | None
    has_simple_single_file: bool
    has_nested_single_file: bool
    has_multiple_files: bool
    files: list[RomFileSchema]
    full_path: str
    created_at: datetime
    updated_at: datetime
    missing_from_fs: bool
    siblings: list[SiblingRomSchema]
    rom_user: RomUserSchema
    merged_screenshots: list[str]
    merged_ra_metadata: RomRAMetadata | None

